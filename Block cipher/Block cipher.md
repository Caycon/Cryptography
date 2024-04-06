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
