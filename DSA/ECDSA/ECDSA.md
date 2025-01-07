# Báo cáo về Elliptic Curve Digital Signature Algorithm (ECDSA)

## 1. Giới thiệu ECDSA
ECDSA (Elliptic Curve Digital Signature Algorithm) là một phiên bản cải tiến của DSA, sử dụng các đường cong elliptic để tăng cường hiệu quả và bảo mật. ECDSA được chuẩn hóa bởi tổ chức NIST và là một phần của tiêu chuẩn ANSI X9.62.

### Lý do sử dụng ECDSA:
- **Hiệu quả cao**: Độ bảo mật tương đương với DSA hoặc RSA nhưng yêu cầu độ dài khóa ngắn hơn.
- **Ứng dụng rộng rãi**: Được sử dụng trong blockchain, chứng chỉ số và các giao thức bảo mật như TLS, SSH.

---

## 2. Cách thức hoạt động của ECDSA
ECDSA hoạt động dựa trên các phép toán trên đường cong elliptic trên trường hữu hạn (finite field). Nó bao gồm hai quy trình chính:
- **Tạo chữ ký số**: Sử dụng khóa riêng để ký một thông điệp.
- **Xác minh chữ ký số**: Sử dụng khóa công khai để kiểm tra tính hợp lệ của chữ ký.

---

## 3. Các bước toán học trong ECDSA
### a. Khởi tạo tham số
1. **Đường cong elliptic**:
   - Một đường cong elliptic trên trường hữu hạn $( \mathbb{F}_p )$ được định nghĩa bởi phương trình:
     $[
     y^2 = x^3 + ax + b \mod p
     $]
     với $(a, b \in \mathbb{F}_p)$, sao cho $(4a^3 + 27b^2 $neq 0 \mod p)$.

2. **Điểm sinh $(G)$**:
   - Chọn một điểm sinh $(G)$ trên đường cong có bậc $(n)$, sao cho $(nG = O)$, với $(O)$ là điểm vô hạn.

3. **Tham số công khai**:
   - $(p)$: Số nguyên tố xác định trường hữu hạn.
   - $(a, b)$: Hệ số của đường cong elliptic.
   - $(G)$: Điểm sinh.
   - $(n)$: Bậc của $(G)$.

### b. Tạo khóa
- **Khóa riêng (private key)**: Một số ngẫu nhiên $(d)$ sao cho $(1 \leq d < n)$.
- **Khóa công khai (public key)**: Tính $(Q = dG)$, với $(Q)$ là điểm trên đường cong.

### c. Quy trình ký số
1. Chọn một số ngẫu nhiên $(k)$ sao cho $(1 \leq k < n)$.
2. Tính:
   - $(R = kG)$, với $(R = (x_1, y_1))$.
   - $(r = x_1 \mod n)$. Nếu $(r = 0)$, chọn lại $(k)$.
3. Tính $(s)$:
   $[
   s = k^{-1} \cdot (H(m) + d \cdot r) \mod n
   $]
   Nếu $(s = 0)$, chọn lại $(k)$.
4. Chữ ký là cặp $((r, s))$.

### d. Quy trình xác minh chữ ký
1. Kiểm tra $(r, s)$ hợp lệ: $(1 \leq r, s < n)$.
2. Tính:
   - $(w = s^{-1} \mod n)$.
   - $(u_1 = H(m) \cdot w \mod n)$.
   - $(u_2 = r \cdot w \mod n)$.
   - $(P = u_1G + u_2Q)$, với $(P = (x_2, y_2))$.
   - $(v = x_2 \mod n)$.
3. Chữ ký hợp lệ nếu $(v = r)$.

---x    