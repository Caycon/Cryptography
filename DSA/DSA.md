# Digital Signature Algorithm
- **DSA** hay **Digital Signature Algorithm** là giải thuật chữ ký số theo chuẩn của chính phủ Mỹ hoặc FIPS cho các chữ ký số.

## 1. Giới thiệu DSA
- **Digital Signature Algorithm (DSA)** là một thuật toán mã hóa bất đối xứng được sử dụng để tạo chữ ký số. DSA được phát triển vào năm 1991 bởi Cơ quan An ninh Quốc gia Hoa Kỳ (NSA) và được công bố như một tiêu chuẩn chữ ký số (Digital Signature Standard - DSS) bởi Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST) vào năm 1993.

---

## 2. Nguyên tắc hoạt động của DSA
DSA dựa trên bài toán logarit rời rạc (Discrete Logarithm Problem - DLP), bao gồm hai quy trình chính:
- **Tạo chữ ký số**: Dùng khóa riêng (private key) để tạo chữ ký cho một thông điệp.
- **Xác minh chữ ký số**: Dùng khóa công khai (public key) để kiểm tra tính hợp lệ của chữ ký.

---

## 3. Quy trình
### a. Khởi tạo tham số
- Chọn một **số nguyên tố $(p)$** lớn (1024-bit hoặc cao hơn).
- Chọn một số nguyên tố $(q)$, sao cho $(q)$ là ước nguyên tố của $(p-1)$ (thông thường, $(q)$ có độ dài 160-bit).
- Chọn một số nguyên $(g)$ có bậc $(q)$ modulo $(p)$, nghĩa là $(g^{q} \mod p = 1)$.

### b. Tạo khóa
- **Khóa riêng (private key)**: Chọn một số ngẫu nhiên $(x)$ (1 < $(x)$ < $(q)$).
- **Khóa công khai (public key)**: Tính $(y = g^x \mod p)$.

### c. Quy trình ký số
1. Chọn một số ngẫu nhiên $(k)$ (1 < $(k)$ < $(q)$).
2. Tính giá trị:
   - $(r = (g^k \mod p) \mod q)$.
   - $(s = k^{-1} \cdot (H(m) + x \cdot r) \mod q)$, với $(H(m))$ là hash của thông điệp.
3. Cặp chữ ký là $((r, s))$.

### d. Quy trình xác minh chữ ký
1. Kiểm tra $(r, s)$ nằm trong khoảng hợp lệ $((1 < r, s < q))$.
2. Tính:
   - $(w = s^{-1} \mod q)$.
   - $(u_1 = H(m) \cdot w \mod q)$.
   - $(u_2 = r \cdot w \mod q)$.
   - $(v = ((g^{u_1} \cdot y^{u_2}) \mod p) \mod q)$.
3. Nếu $(v = r)$, chữ ký hợp lệ.

---

## 4. Ưu điểm của DSA
- **Tính bảo mật cao**: Dựa trên bài toán logarit rời rạc.
- **Hiệu suất tốt**: DSA được tối ưu hóa để ký số nhanh hơn so với RSA.
- **Tiêu chuẩn hóa**: Được công nhận bởi NIST và sử dụng rộng rãi trong các giao thức bảo mật (TLS, SSH).

---

## 5. Nhược điểm của DSA
- **Phụ thuộc vào số ngẫu nhiên $(k)$**: Nếu $(k)$ bị rò rỉ hoặc sử dụng lại, khóa riêng $(x)$ có thể bị khôi phục.
- **Khả năng mở rộng hạn chế**: Độ dài khóa thấp hơn RSA và ECDSA khi xét cùng mức độ bảo mật.
- **Bảo mật yếu nếu không dùng hàm băm mạnh**: Hash yếu có thể làm suy yếu tính toàn vẹn của chữ ký.

---

## 6. Ứng dụng của DSA
- **Xác thực chữ ký số**: Sử dụng trong các chứng chỉ số, ví dụ: X.509.
- **Bảo mật giao thức**: DSA là thành phần quan trọng trong giao thức SSH và TLS.
- **Blockchain**: Một số blockchain sử dụng DSA hoặc các biến thể để xác thực giao dịch.

---

## 7. So sánh với các thuật toán khác

| Thuật toán    | Tính năng nổi bật       | Tốc độ ký số   | Tốc độ xác minh | Độ dài khóa     |
|---------------|-------------------------|----------------|-----------------|-----------------|
| **DSA**       | Bảo mật cao, tiêu chuẩn hóa | Nhanh hơn RSA  | Chậm hơn RSA    | 1024-3072 bit   |
| **ECDSA**     | Hiệu quả với khóa nhỏ   | Nhanh hơn DSA  | Nhanh hơn DSA   | 256-521 bit     |
| **RSA**       | Đơn giản, phổ biến      | Chậm hơn DSA   | Nhanh hơn DSA   | 2048-4096 bit   |

---