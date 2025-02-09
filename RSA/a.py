from sage.all import *

# Định nghĩa các giá trị
a = 0xc48c998771f7ca68c9788ec4bff9b40b80000  # Các bit ở giữa đã biết của p
n = 0x3ab05d0c0694c6bd8ee9683d15039e2f738558225d7d37f4a601bcb929ccfa564804925679e2f3542b  # RSA modulus
R = 2**16  # Giới hạn trên của các bit chưa biết
t = 148  # Số bit của r_m

# Khởi tạo các biến
x, y = var('x y')

# Đa thức f(x, y) = x + 2^t * y + a
f = x + 2**t * y + a

# Xây dựng lưới
lattice = Matrix(ZZ, [
    [R**3, 0, 0, 0],
    [0, R**3, 2**t * R**3, 0],
    [0, 0, R**3, 0],
    [n, 0, 0, 1]
])

# Giảm cơ sở lưới bằng LLL
reduced_lattice = lattice.LLL()

# Tạo hệ phương trình từ các vector giảm
eqs = []
for row in reduced_lattice.rows():
    eq = sum(c*v for c, v in zip(row, [x, y, R, Integer(1)]))
    eqs.append(eq)

# Giải hệ phương trình để tìm r_t và r_m
roots = [solve(eq, x) for eq in eqs]

# Tạo danh sách các nghiệm của p
p_solutions = [a + r[0] + r[1] * 2**t for r in roots if len(r) == 2]

# Kiểm tra các giá trị của p để tìm ước chung lớn nhất của N
for p in p_solutions:
    q = n // p
    if n % p == 0:
        print(f'Tìm thấy: p = {hex(p)}, q = {hex(q)}')

# In kết quả các nghiệm của p
print(f"Các nghiệm của p: {p_solutions}")
