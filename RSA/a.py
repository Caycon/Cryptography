# """
# CHALLENGE:
# -----------
# Trong challenge này, ta có bài toán RSA với các tham số:
#     - n: module RSA, với n = p * q.
#     - e: số mũ công khai (thông thường e = 65537).
#     - c: bản mã, tính theo c = m^e mod n.
# Ngoài ra, ta có thông tin rò rỉ leak_p của số p, cụ thể leak_p chứa các bit từ vị trí 40 đến 465 của p (với p có 512 bit, 40 bit đầu và 47 bit cuối không được tiết lộ).

# Ý tưởng chính:
# -------------
# Vì leak_p tiết lộ phần giữa của số p, ta có thể biểu diễn p dưới dạng:
#     p = a * x + y + leak_p,
# với:
#     - a = 2^(512 - 47) = 2^465, vì 47 bit cuối không được rò rỉ.
#     - y là số nguyên nhỏ hơn b = 2^47 (tương ứng với 47 bit cuối).
#     - x là ẩn số cần tìm.

# Mục tiêu của ta là tìm được x và y (sau đó tính lại p), từ đó tách số q = n/p và tính khóa riêng RSA để giải mã thông điệp.

# Phương pháp tấn công:
# ----------------------
# 1. **Xây dựng đa thức ban đầu:**
#    Ta có đa thức f(x, y) = a*x + y + leak_p, được biết modulo n.

# 2. **Tạo các đa thức dịch chuyển (shifted polynomials):**
#    Dựa trên đa thức f(x,y) ban đầu, ta xây dựng một số đa thức dịch chuyển theo dạng:
#        - Nếu h == 0: g(x,y) = n * x^i.
#        - Nếu h > 0:  g(x,y) = f(x,y) * x^i * y^(h-1).
#    Các đa thức này có mục đích tạo ra một hệ đa thức có liên hệ với x và y với các hệ số nhỏ sau khi “nâng” theo một số scale nhất định.

# 3. **Xây dựng lattice và áp dụng LLL:**
#    Ta đưa các đa thức dịch chuyển lên một lattice bằng cách “nâng” các hệ số theo scale_x và scale_y để cân bằng độ lớn của các đơn thức.
#    Sau đó, dùng thuật toán LLL để thu được cơ sở lattice với các vector ngắn, từ đó các đa thức tương ứng có hệ số nhỏ.

# 4. **Tách biến và giải hệ đa thức:**
#    Dùng phép tính resultant để loại bỏ một biến (thường là loại bỏ y để có đa thức đơn biến theo x, và ngược lại), sau đó giải các đa thức này để thu được nghiệm x và y.

# 5. **Tính lại p và giải mã RSA:**
#    Tính p = a*x + y + leak_p, từ đó tính số q = n // p. Cuối cùng, tính khóa riêng d và giải mã thông điệp.

# """

# from Crypto.Util.number import long_to_bytes, bytes_to_long
# from sage.all import *

# # ------------------ Bước 1: Khởi tạo tham số RSA và leak_p ------------------
# # Các tham số dưới đây là ví dụ (bạn thay bằng các giá trị thực tế nếu cần)
# n = 167580499956215950519401364953715382046426622073945444209826355141355616253284471005334650342162345240975585728731605368177279851073566181310579765061891014250502756284021540424912815047098023724780350364100609602779707167364816138138292881169029901637887077174119691465839709933394383980487654025215303169197
# e = 65537
# c = 139141713394182175338014160210574677242324318147310823544533218285438453679685360942557889405708630849117917919844618438631772469175157267044325855150684069102771610083706768718034754862646137870042713558761139906496513003195874156227906594994060711022603795992594839895900529076885908269590003750247551274645
# leak_p = 11285951004747532118510977324365459146506394352712787708919871521893387325998280830757079994592547761237824232119473733009976060329355198332928

# # ------------------ Bước 2: Thiết lập biểu diễn ẩn của số p ------------------
# # Ta biểu diễn p theo dạng:
# #    p = a * x + y + leak_p
# # Trong đó:
# #    a = 2^(512 - 47) vì 47 bit cuối của p không được tiết lộ.
# #    y < b, với b = 2^47, đại diện cho 47 bit cuối.
# a = 2**(512 - 47)   # a = 2^465
# b = 2**47           # b = 2^47
# # Biến x cần tìm (và y có giá trị nhỏ)
# # Chọn bậc của các đa thức dịch chuyển, ta chọn deg = 4 (có thể điều chỉnh nếu cần)
# deg = 4

# # ------------------ Bước 3: Xây dựng đa thức ban đầu f(x, y) ------------------
# # Ta làm việc trên trường số nguyên modulo n, để đảm bảo các đa thức "ẩn" đồng nhất theo modulo n.
# Pxy = PolynomialRing(Zmod(n), names=('x', 'y'))
# x_mod, y_mod = Pxy.gens()
# # Đa thức ban đầu: f(x, y) = a*x + y + leak_p
# Pol_mod = a * x_mod + y_mod + leak_p
# # Chuyển hệ số về ZZ (số nguyên) để thuận tiện cho các thao tác tiếp theo
# Pol_int = Pol_mod.change_ring(ZZ)
# PR_int = Pol_int.parent()  # Không gian đa thức với hệ số nguyên
# x, y = PR_int.gens()       # Lấy các biến x và y

# # ------------------ Bước 4: Tạo các đa thức dịch chuyển ------------------
# # Ta tạo các đa thức dịch chuyển dựa trên các cặp số mũ (h, i) sao cho h + i <= deg.
# # Điều này tạo ra một hệ các đa thức với số lượng vừa đủ để áp dụng tấn công lattice.
# exponent_pairs = [(k - i, i) for k in range(deg + 1) for i in range(k + 1)]
# # Tạo danh sách các đơn thức tương ứng: mỗi đơn thức có dạng x^(h)*y^(i)
# monomials = [PR_int(x**h * y**i) for (h, i) in exponent_pairs]

# # f_poly là đa thức gốc f(x, y)
# f_poly = Pol_int

# # Tạo danh sách các đa thức dịch chuyển g_list theo quy tắc:
# #   - Nếu h == 0: g(x,y) = n * x^i
# #   - Nếu h > 0:  g(x,y) = f(x,y) * x^i * y^(h - 1)
# g_list = []
# for (h, i) in exponent_pairs:
#     if h == 0:
#         # Khi h == 0, ta nhân với n để đảm bảo đa thức chia hết cho n.
#         g_poly = n * (x**i)
#     else:
#         # Khi h > 0, nhân f(x,y) với x^i * y^(h-1)
#         g_poly = f_poly * (x**i * y**(h - 1))
#     g_list.append(g_poly)

# # ------------------ Bước 5: Xây dựng lattice từ các đa thức dịch chuyển ------------------
# # Mục tiêu: "Nâng" các hệ số của các đa thức sao cho chúng có độ lớn tương đương, từ đó
# # ta đưa chúng vào một ma trận lattice. Sau đó, áp dụng LLL để thu được vector có hệ số nhỏ.
# #
# # Chọn các hằng số scale:
# #    scale_x: dùng để nâng các hệ số của các đơn thức theo biến x.
# #             Ở đây, scale_x = 2^(512 - 472) = 2^40 (vì 40 bit đầu của p không được tiết lộ).
# #    scale_y: dùng cho biến y, ta để scale_y = b = 2^47.
# scale_x = 2**(512 - 472)  # scale_x = 2^40
# scale_y = b             # scale_y = 2^47

# # Số lượng đa thức dịch chuyển (số hàng của lattice)
# m_size = len(g_list)
# # Khởi tạo ma trận lattice M kích thước m_size x m_size với hệ số nguyên.
# M = Matrix(ZZ, m_size, m_size)
# for row in range(m_size):
#     for col in range(m_size):
#         # Với cặp số mũ (h, i) ứng với cột col,
#         # lấy hệ số của đơn thức x^h * y^i trong đa thức g_list[row].
#         (h, i) = exponent_pairs[col]
#         coeff = g_list[row][h, i]
#         # "Nâng" hệ số theo scale_x^h và scale_y^i để cân bằng các đơn thức khi đưa vào lattice.
#         M[row, col] = coeff * (scale_x ** h) * (scale_y ** i)

# # ------------------ Bước 6: Áp dụng thuật toán LLL ------------------
# # LLL (Lenstra–Lenstra–Lovász) sẽ tìm được một cơ sở lattice với các vector có độ dài ngắn.
# # Những vector này tương ứng với các đa thức có hệ số "nhỏ", giúp chúng ta dễ dàng truy xuất nghiệm.
# B = M.LLL()

# # ------------------ Bước 7: Tái tạo các đa thức ẩn từ cơ sở lattice ------------------
# # Mỗi hàng của ma trận B sau LLL được dùng để tái tạo lại một đa thức ẩn H[i] với hệ số nguyên.
# # Ta cần "điều chỉnh" các hệ số bằng cách chia lại theo giá trị của đơn thức tại (scale_x, scale_y).
# H = {}  # H[i] chứa đa thức tương ứng với hàng thứ i của cơ sở lattice B.
# for i in range(B.nrows()):
#     poly_H = PR_int(0)  # Khởi tạo đa thức không.
#     for j in range(B.ncols()):
#         # monomials[j] là đơn thức ban đầu ứng với cột j.
#         # B[i, j] là hệ số sau LLL.
#         # Chia cho giá trị của monomials[j] tại (scale_x, scale_y) để cân bằng đơn thức.
#         poly_H += PR_int((monomials[j] * B[i, j]) / monomials[j](scale_x, scale_y))
#     H[i] = poly_H

# # ------------------ Bước 8: Tách biến và giải hệ đa thức ------------------
# # Sử dụng phép tính resultant để loại bỏ một biến khỏi hệ đa thức, từ đó thu được đa thức đơn biến.
# #
# # Tạo các polynomial ring đơn biến cho x và y:
# PX = PolynomialRing(ZZ, 'xs')
# xs = PX.gen()
# PY = PolynomialRing(ZZ, 'ys')
# ys = PY.gen()

# # --- Loại bỏ biến y để có đa thức theo x ---
# # Tính resultant của H[0] và H[1] theo biến y.
# res_x1 = H[0].resultant(H[1], y).subs(x=xs)
# # Tính thêm resultant của H[0] và H[2] theo biến y.
# res_x2 = H[0].resultant(H[2], y).subs(x=xs)
# # Lấy ước chung lớn nhất (gcd) của hai đa thức trên, giúp loại bỏ nhiễu từ các nghiệm không cần thiết.
# poly_x = gcd(res_x1, res_x2)
# # Lấy nghiệm đầu tiên của poly_x (trong trường hợp có nhiều nghiệm, bạn có thể kiểm tra lại)
# x_root = poly_x.roots()[0][0]
# # Ép về kiểu số nguyên Python (nếu cần)
# try:
#     x_root = int(x_root.lift())
# except AttributeError:
#     x_root = int(x_root)

# # --- Loại bỏ biến x để có đa thức theo y ---
# res_y1 = H[0].resultant(H[1], x).subs(y=ys)
# res_y2 = H[0].resultant(H[2], x).subs(y=ys)
# poly_y = gcd(res_y1, res_y2)
# y_root = poly_y.roots()[0][0]
# # Ép về kiểu số nguyên Python
# try:
#     y_root = int(y_root.lift())
# except AttributeError:
#     y_root = int(y_root)

# # ------------------ Bước 9: Tính lại số p và tách số q ------------------
# # Từ nghiệm x_root và y_root, tính lại số p theo công thức:
# #    p = a*x + y + leak_p.
# recovered_p = a * x_root + y_root + leak_p
# # Số q được tính bằng: q = n // p.
# recovered_q = n // recovered_p

# # ------------------ Bước 10: Tính khóa riêng và giải mã thông điệp RSA ------------------
# # Khóa riêng d được tính là số nghịch đảo của e modulo lcm(p-1, q-1).
# d = pow(e, -1, lcm(recovered_p - 1, recovered_q - 1))
# # Giải mã thông điệp: tính m = c^d mod n.
# m_int = pow(c, d, n)
# print(long_to_bytes(int(m_int)))


from Crypto.Util.number import *

p= getPrime(512)
q= getPrime(512)
n= p*q
e= 65537
flag= b'I_don_t_known_what_to_write_here'
m= bytes_to_long(flag)
phi= (p- 1)*(q- 1)
d= pow(e, -1, phi)
leak_d= int(bin(d)[500:], 2)
c= pow(m,e,n)
print(f'{n= }')
print(f'{e= }')
print(f'{c= }')
print(f'{leak_d= }')
print(f'{d= }')


#!/usr/bin/env python3
import math
from Crypto.Util.number import long_to_bytes

# --- Input parameters (obtained from the challenge) ---
# For example, the challenge prints these values:
# n = <big integer>
# e = 65537
# c = <big integer>
# leak_d = <big integer> (this is bin(d)[400:] interpreted as an integer)
#
# In an actual challenge these would be provided; here we assume they are read from a file or input.
#
# For demonstration, let’s assume we have the following variables:
# (Replace the ... with the actual numbers.)
n = ...      # the RSA modulus
e = 65537    # public exponent
c = ...      # RSA ciphertext
leak_d = ... # the leaked part of d (the low bits after the 400th bit)

# --- Setup ---
# We know that d is about as large as n (which is 1024 bits, since p,q are 512 bits)
# and the leak is produced by: leak_d = int(bin(d)[400:], 2)
# So if we let D = d.bit_length(), then the number of missing (unknown) bits is R = D - 400.
# Typically D ≈ n.bit_length() (≈ 1024), so we take:
D = len(bin(n)) - 2  # number of bits in n
R = D - 500  # so here R is roughly 624

# We also know that:
#    d = X * 2^R + leak_d,
# where X is the unknown 400-bit number.

# Our RSA equation is: e*d - k*phi(n) = 1.
# Note that for RSA, phi(n) = (p-1)(q-1) and k is a small positive integer.
# In fact, since d is “full‐size”, one typically has d ~ n so that k ≈ e.
#
# We now try candidates for k in a small interval around e.

delta = 65537  # search window around e (tweak if needed)
found = False
candidate_d = None

for k in range(e - delta, e + delta):
    if k <= 0:
        continue
    # The RSA relation gives: e*d ≡ 1 (mod k) so we expect d ≈ k*n/e.
    d_approx = (k * n) // e
    # Write d = X*2^R + leak_d, so an approximate X is:
    x_approx = (d_approx - leak_d) >> R  # equivalent to floor((d_approx - leak_d)/2^R)
    
    # Try a few offsets around x_approx
    for offset in range(-5, 6):
        X = x_approx + offset
        if X < 0:
            continue
        d_candidate = X * (1 << R) + leak_d
        # Check that the RSA relation holds: e*d_candidate - 1 must be divisible by k.
        if (e * d_candidate - 1) % k != 0:
            continue
        phi_candidate = (e * d_candidate - 1) // k
        
        # Recover p+q from phi(n) = n - (p+q) + 1  =>  p+q = n - phi_candidate + 1
        s = n - phi_candidate + 1
        # For correct p,q, the discriminant Δ = (p+q)^2 - 4n must be a perfect square.
        disc = s * s - 4 * n
        if disc < 0:
            continue
        sqrt_disc = math.isqrt(disc)
        if sqrt_disc * sqrt_disc != disc:
            continue

        # Now compute p and q.
        p = (s + sqrt_disc) // 2
        q = (s - sqrt_disc) // 2
        if p * q == n:
            print("[+] Factors found!")
            print("p =", p)
            print("q =", q)
            found = True
            break
    if found:
        break

if not found:
    print("[-] Failed to recover the key!")
    exit(1)

# We now have candidate d = d_candidate.
print("[+] Recovered d.")

# Decrypt the ciphertext:
m = pow(c, d_candidate, n)
flag = long_to_bytes(int(m))
print("[+] Decrypted message:")
print(flag.decode())
