# Feistel
- Feistel là một cấu trúc mã hóa khối được thiết kế bởi Horst Feistel và Don Coppersmith vào năm 1973. Feistel chia plaintext thành các khối dữ liệu sau đó mã hóa trên từng khối, thực hiện thông qua n rounds, gồm các bước thay thế và chuyển vị trên dữ liệu đầu vào.
![image](https://hackmd.io/_uploads/B1Nrjo7c6.png)
- Các bước cụ thể như sau:
    - Quá trình mã hóa nhận vào một khối dữ liệu plaintext và một master key.
    - Chia khối đó thành hai phần bằng nhau, nửa trái kí hiệu L0, nửa phải kí hiệu R0.
    - Lặp qua n rounds (i:1->n) để mã hóa, các round sử dụng chung hàm mã hóa F nhưng khác sub-key $K_i$ (được sinh từ master key). Thực hiện các bước sau đây:
    - $L_{i+1}= R_i$
    - $R_{i+1}= L_i ⊕ F(R_i, K_i)$
    - Sau n rounds, thực hiện swap Ln, Rn và gộp lại để thu giá trị mã hóa: $R_n L_n$.
    - Để giải mã, ta thực hiện ngược lại quá trình trên.

- Một số lưu ý cho Feistel:

- Kích thước block càng lớn càng an toàn tuy nhiên có thể ảnh hưởng đến tốc độ tính toán. Tương tự với kích thước Key.
- Sử dụng nhiều round giúp tăng khả năng bảo mật.
- Hàm sinh sub-key từ master key có độ phức tạp càng cao thì càng khó bị phân tích mã. Tương tự với hàm F.
# Data Encryption Standard- DES
## Introduct
- DES là chuẩn mã hóa dữ liệu do cơ quan An ninh Quốc gia Hoa Kỳ (NSA) đề xuất cuối những năm 1970. DES sử dụng cấu trúc mã hóa Feistel với 16 rounds, kích thước mỗi khối là 64 bits, kích thước khóa là 56 bits. Tương tự Feistel, DES sử dụng một hàm F chung trong khi mỗi round lại sử dụng một sub-key riêng (được sinh từ master key).
- Đầu tiên, khối plaintext (64 bits) được đưa qua bước Initial permutation để thực hiện hoán vị các bit data (Quy tắc hoán vị được định nghĩa trong một bảng gọi là Inital permutaion table). Sau đó, cho khối chạy 16 rounds để mã hóa, các bước chạy giống như Feistel đã trình bày ở trên. Cuối cùng, thực hiện bước Final permutation để thu ciphertext (bước này thực chất là đảo ngược của quá trình Initial permutation).
![image](https://hackmd.io/_uploads/HJvZoiQ5p.png)
## Cơ chế hoạt động 
- Sinh khóa cho các round:
    - Khóa đầu vào thực chất có tới 64 bits nhưng bị loại bỏ các bit ở vị trí 8i (8, 16, 24, …) nên còn lại 56 bits. 
    - Đầu tiên, 64-bit key sẽ được đưa qua bước Permuted choice 1, thực hiện bỏ đi các bit ở vị trí 8i và hoán vị theo quy tắc định trước (Theo bảng Permuted table 1), thu được 56-bit key. 
    - Tách 56-bit key thành 2 phần bằng nhau (28 bits), nửa bên trái là C0, nửa bên phải là D0. Tiếp theo, lặp 16 lần để tạo 16 subkeys, mỗi lần thực hiện dịch trái xoay vòng Ci, Di từ 1 đến 2 bits (Số bit cần dịch cụ thể cho mỗi round xem ảnh đính kèm). 
    - Sau khi dịch, thực hiện tiếp bước Permuted choice 2 để thu được subkey cho round i. Permuted choice 2 cho ra 48-bit key.
![image](https://hackmd.io/_uploads/HyloAsXcp.png)
- Hàm Feistel F:
    - Hàm F trong DES được định nghĩa như sau:

    $$F(K_i, R_{i-1}) = P(S(E(R_{i-1}) ⊕ (K_i)))$$
    - Mở rộng: 32 bit đầu vào được mở rộng thành 48 bit sử dụng thuật toán hoán vị mở rộng (expansion permutation) với việc nhân đôi một số bit. Giai đoạn này được ký hiệu là E trong sơ đồ.
    - Trộn khóa: 48 bit thu được sau quá trình mở rộng được XOR với khóa con. Mười sáu khóa con 48 bit được tạo ra từ khóa chính 56 bit theo một chu trình tạo khóa con (key schedule) miêu tả ở phần sau.
    - Thay thế: 48 bit sau khi trộn được chia làm 8 khối con 6 bit và được xử lý qua hộp thay thế S-box. Đầu ra của mỗi khối 6 bit là một khối 4 bit theo một chuyển đổi phi tuyến được thực hiện bằng một bảng tra. Khối S-box đảm bảo phần quan trọng cho độ an toàn của DES. Nếu không có S-box thì quá trình sẽ là tuyến tính và việc thám mã sẽ rất đơn giản.
    - Hoán vị: Cuối cùng, 32 bit thu được sau S-box sẽ được sắp xếp lại theo một thứ tự cho trước (còn gọi là P-box).
    - Quá trình luân phiên sử dụng S-box và sự hoán vị các bít cũng như quá trình mở rộng đã thực hiện được tính chất gọi là sự xáo trộn và khuếch tán (confusion and diffusion). Đây là yêu cầu cần có của một thuật toán mã hoá được Claude Shannon phát hiện trong những năm 1940.
![image](https://hackmd.io/_uploads/SJ6f00rq6.png)
    - Trong đó, E là hàm mở rộng, dùng để biến đổi 32-bit dữ liệu đầu vào thành 48 bits (bằng kích thước khóa). Hàm S là các hộp S-box thực hiện thay thế đầu vào. Hàm P là hộp P-box thực hiện hoán vị đầu vào.
- Nhìn chung DES sẽ hoạt động như sau:
![image](https://hackmd.io/_uploads/H1z7JkUqa.png)
