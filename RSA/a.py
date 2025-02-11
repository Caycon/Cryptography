from Crypto.Util.number import *

e = 65537
n = 95833140363150173085400781562336570561015616460313210023975270126616157131624528587272063057307225026161835408699888323499488279019129501329065630402087285258471135141986496693723213866761952112220188009361594959340470056360323997143701160632189890086147838319540477404939016199414749172031337591306156717957
leak_p = 446726636560982512156094109972620717668814180129313191107990193476358979707694308539854517523276106719891732860421584561376386167782984646656
c = 85585941751998800537891696785955548411294697759152457743742952506986880949373120940602110913029788782243069830692032701804087815911677859038561767938618923528464864146810669499058733566518068351509560838577248261272216817539613495749072417594986788748418531887477297026449652895516064864083462020309481181862

PR = PolynomialRing(Zmod(n), names=('x', 'y'))
x, y = PR.gens()
pol = 2**(512- 47)* x + y + leak_p

XX= 2**(512-472)
YY= 2**47
degree=4
n = pol.parent().characteristic()
f = pol.change_ring(ZZ)
PR, (x, y) = f.parent().objgens()

idx = [(k - i, i) for k in range(degree + 1) for i in range(k + 1)]
monomials = [PR(x**t[0] * y**t[1]) for t in idx]

g = [y**h * x**i * n if h == 0 else y**(h - 1) * x**i * f for h, i in idx]

M = Matrix(ZZ, len(g))
for row in range(M.nrows()):
    for col in range(M.ncols()):
        h, i = idx[col]
        M[row, col] = g[row][h, i] * XX**h * YY**i

B = M.LLL()
PX, PY = PolynomialRing(ZZ, 'xs'), PolynomialRing(ZZ, 'ys')
xs, ys = PX.gen(), PY.gen()

H = {i: PR(0) for i in range(B.nrows())}
for i in range(B.nrows()):
    for j in range(B.ncols()):
        H[i] += PR((monomials[j] * B[i, j]) / monomials[j](XX, YY))

poly_x = gcd(H[0].resultant(H[1], y).subs(x=xs), H[0].resultant(H[2], y).subs(x=xs))
x_root = poly_x.roots()[0][0]

poly_y = gcd(H[0].resultant(H[1], x).subs(y=ys), H[0].resultant(H[2], x).subs(y=ys))
y_root = poly_y.roots()[0][0]
x= x_root
y= y_root
p = 2**(512-47) * x + y + leak_p
q = n // p
assert p * q == n, 'Factoring failed'

d = pow(e, -1, lcm(p - 1, q - 1))
m = pow(c, d, n)

print(long_to_bytes(int(m)))




from Crypto.Util.number import long_to_bytes
from sage.all import Matrix, PolynomialRing, Zmod, ZZ, gcd, lcm

e = 65537
n = 95833140363150173085400781562336570561015616460313210023975270126616157131624528587272063057307225026161835408699888323499488279019129501329065630402087285258471135141986496693723213866761952112220188009361594959340470056360323997143701160632189890086147838319540477404939016199414749172031337591306156717957
leak_p= 446726636560982512156094109972620717668814180129313191107990193476358979707694308539854517523276106719891732860421584561376386167782984646656
c= 85585941751998800537891696785955548411294697759152457743742952506986880949373120940602110913029788782243069830692032701804087815911677859038561767938618923528464864146810669499058733566518068351509560838577248261272216817539613495749072417594986788748418531887477297026449652895516064864083462020309481181862

# --- Các tham số cho phép toán đa thức và lattice ---
# a và b dùng để biểu diễn ẩn dưới dạng: p = a * x + y + leak_p
a = 2**(512 - 47)   # 2^(465)
b  = 2**47           # 2^(47)
deg = 4         # bậc tối đa dùng trong thuật toán

# --- Xây dựng đa thức ban đầu ---
# Tạo polynomial ring hai biến trên Zmod(n)
Pxy = PolynomialRing(Zmod(n), names=('x', 'y'))
x_mod, y_mod = Pxy.gens()

# Đa thức ban đầu: f(x, y) = a * x + y + leak_p
Pol_mod = a * x_mod + y_mod + leak_p

# Chuyển sang đa thức có hệ số nguyên
Pol_int = Pol_mod.change_ring(ZZ)
PR_int, (x, y) = Pol_int.parent().objgens()

# --- Xây dựng hệ chỉ số và các đơn thức ---
# Danh sách các cặp số mũ (h, i) với tổng bậc <= deg
exponent_pairs = [(k - i, i) for k in range(deg + 1) for i in range(k + 1)]
# Danh sách các đơn thức tương ứng: x^(h) * y^(i)
monomials = [PR_int(x**h * y**i) for (h, i) in exponent_pairs]

# f_poly là đa thức chuyển sang hệ số nguyên
f_poly = Pol_int

# --- Xây dựng các đa thức dịch chuyển (shifted polynomials) ---
# Theo công thức:
#   Nếu h == 0: g(x,y) = n * x^i
#   Nếu h > 0:  g(x,y) = f_poly * x^i * y^(h-1)
g_list = []
for (h, i) in exponent_pairs:
    if h == 0:
        g_poly = n * (x**i)
    else:
        g_poly = f_poly * (x**i * y**(h - 1))
    g_list.append(g_poly)

# --- Xây dựng ma trận lattice ---
# Các hệ số được “nâng” lên bằng scale_x và scale_y
scale_x = 2**(512 - 472)  # 2^(40)
scale_y = b           # 2^(47)
m_size = len(g_list)

M = Matrix(ZZ, m_size, m_size)
for row in range(m_size):
    for col in range(m_size):
        # Với cặp (h, i) ứng với cột col, lấy hệ số của x^h*y^i trong g_list[row]
        (h, i) = exponent_pairs[col]
        coeff = g_list[row][h, i]
        M[row, col] = coeff * (scale_x ** h) * (scale_y ** i)

# --- Giảm LLL cho lattice ---
B = M.LLL()

# --- Tái tạo các đa thức “ẩn” từ cơ sở LLL ---
H = {}  # H[i] sẽ lưu đa thức tương ứng với hàng thứ i của B
for i in range(B.nrows()):
    poly_H = PR_int(0)
    for j in range(B.ncols()):
        # Cân bằng đơn thức bằng cách chia cho giá trị tại (scale_x, scale_y)
        poly_H += PR_int((monomials[j] * B[i, j]) / monomials[j](scale_x, scale_y))
    H[i] = poly_H

# --- Tách biến: tính resultant để loại bỏ biến còn lại ---
# Tạo 2 polynomial ring univariate mới (cho x và cho y)
PX = PolynomialRing(ZZ, 'xs')
xs = PX.gen()
PY = PolynomialRing(ZZ, 'ys')
ys = PY.gen()

# Tìm đa thức theo x bằng cách loại y:
res_x1 = H[0].resultant(H[1], y).subs(x=xs)
res_x2 = H[0].resultant(H[2], y).subs(x=xs)
poly_x = gcd(res_x1, res_x2)
# Lấy nghiệm đầu tiên
x_root = poly_x.roots()[0][0]
# Ép x_root về kiểu số nguyên Python (nếu cần)
try:
    x_root = int(x_root.lift())
except AttributeError:
    x_root = int(x_root)

# Tương tự, tìm đa thức theo y bằng cách loại x:
res_y1 = H[0].resultant(H[1], x).subs(y=ys)
res_y2 = H[0].resultant(H[2], x).subs(y=ys)
poly_y = gcd(res_y1, res_y2)
y_root = poly_y.roots()[0][0]
# Ép y_root về kiểu số nguyên Python
try:
    y_root = int(y_root.lift())
except AttributeError:
    y_root = int(y_root)

# --- Tái tạo ước số p của RSA ---
recovered_p = a * x_root + y_root + leak_p
recovered_q = n // recovered_p

# --- Tính khóa riêng và giải mã ---
d = pow(e, -1, lcm(recovered_p - 1, recovered_q - 1))
m = pow(c, d, n)

# Ép m về kiểu số nguyên Python (nếu cần)
try:
    m = int(m.lift())
except AttributeError:
    m = int(m)

print(long_to_bytes(m))
