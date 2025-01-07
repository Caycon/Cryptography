# Elliptic Curve Digital Signature Algorithm (ECDSA)

## 1. Giới thiệu ECDSA
- **ECDSA (Elliptic Curve Digital Signature Algorithm)** là một phiên bản cải tiến của DSA, sử dụng các đường cong elliptic để tăng cường hiệu quả và bảo mật. ECDSA được chuẩn hóa bởi tổ chức NIST và là một phần của tiêu chuẩn ANSI X9.62.

---

## 2. Cách thức hoạt động của ECDSA
- **ECDSA** hoạt động dựa trên các phép toán trên đường cong elliptic trên trường hữu hạn (finite field). - Nó bao gồm hai quy trình chính:
- **Tạo chữ ký số**: Sử dụng khóa riêng để ký một thông điệp.
- **Xác minh chữ ký số**: Sử dụng khóa công khai để kiểm tra tính hợp lệ của chữ ký.

---

## 3. Nguyên tắc hoạt động
### a. Khởi tạo tham số
1. **Đường cong elliptic**:
   - Một đường cong elliptic trên trường hữu hạn $( \mathbb{F}_p )$ được định nghĩa bởi phương trình:
     $[
     y^2 = x^3 + ax + b \mod p
     $]
     với $(a, b \in \mathbb{F}_p)$, sao cho $(4a^3 + 27b^2 \neq 0 \mod p)$.

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

---

# Attack

---

## 1. Nonce Reuse Attack
### Dấu hiệu
- Nếu số ngẫu nhiên $(k)$ được sử dụng lại cho hai thông điệp khác nhau, khóa riêng $(d)$ có thể bị khôi phục.

### Nguyên lý hoạt động:
1. Với hai chữ ký $( (r, s_1) )$ và $( (r, s_2) )$ từ cùng một $(k)$, ta có:
   $[
   s_1 - s_2 = k^{-1} \cdot (H(m_1) - H(m_2)) \mod n
   ]$
2. Suy ra $(k)$:
   $[
   k = \frac{H(m_1) - H(m_2)}{s_1 - s_2} \mod n
   ]$
3. Sử dụng $(k)$ để tính khóa riêng $(d)$:
   $[
   d = \frac{s \cdot k - H(m)}{r} \mod n
   ]$

### Fix:
- Đảm bảo mỗi lần ký sử dụng một số ngẫu nhiên $(k)$ khác nhau, không bao giờ tái sử dụng.

---

## 2. Nonce Leakage Attack
### Dấu hiệu
- Nếu số ngẫu nhiên $(k)$ bị rò rỉ, khóa riêng $(d)$ có thể dễ dàng tính được từ chữ ký.

### Nguyên lý hoạt động:
1. Biết $(k)$, tính $(d)$ từ công thức:
   $[
   d = \frac{s \cdot k - H(m)}{r} \mod n
   ]$

### Fix:
- Bảo vệ giá trị $(k)$ bằng cách sử dụng bộ sinh số ngẫu nhiên bảo mật (CSPRNG).

---

## 3. Side-Channel Attack
### Dấu hiệu
- Kẻ tấn công có thể khai thác thông tin từ quá trình tính toán, như thời gian thực thi hoặc năng lượng tiêu thụ, để suy ra khóa riêng.

### Ví dụ:
- **Tấn công dựa trên thời gian (Timing Attack)**: Phân tích thời gian thực thi của các phép toán modulo để suy ra thông tin về khóa riêng.
- **Tấn công năng lượng (Power Analysis Attack)**: Đo năng lượng tiêu thụ của thiết bị trong quá trình ký số để khôi phục $(k)$.

### Fix:
- Sử dụng các thuật toán hằng thời gian và kỹ thuật làm mờ (blinding) để ngăn chặn rò rỉ thông tin.

---

## 4. Implementation Flaw Attack
### Dấu hiệu
- Lỗi trong triển khai, chẳng hạn sử dụng các tham số không chuẩn hoặc phép tính modulo sai, có thể dẫn đến việc rò rỉ khóa riêng.

### Ví dụ:
- Sử dụng đường cong không chuẩn với tính chất yếu, dễ bị tấn công toán học.
- Tính $(s)$ hoặc $(r)$ không đúng cách.

### Fix:
- Sử dụng các đường cong chuẩn hóa như P-256, P-384, P-521.
- Kiểm tra cẩn thận tính đúng đắn của thuật toán triển khai.

---

## 5. Hash Collision Attack
### Dấu hiệu
- Nếu hàm băm $(H(m))$ có điểm yếu và cho phép tạo hai thông điệp $(m_1, m_2)$ với cùng giá trị $(H(m_1) = H(m_2))$, kẻ tấn công có thể giả mạo chữ ký.

### Fix:
- Sử dụng các hàm băm bảo mật như SHA-256 hoặc SHA-3.
- Tránh sử dụng các hàm băm cũ như MD5 hoặc SHA-1.

---

## 6. Weak or Malicious Curve Attack
### Dấu hiệu
- Các đường cong không chuẩn hoặc được chọn bởi kẻ tấn công có thể chứa điểm yếu cố tình, cho phép khôi phục khóa riêng.

### Fix:
- Chỉ sử dụng các đường cong chuẩn được công nhận bởi NIST hoặc SECG.
- Không sử dụng các đường cong tùy chỉnh trừ khi đã được kiểm tra độc lập.

---
