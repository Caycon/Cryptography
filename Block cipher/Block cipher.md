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
## Giải mã
- Quá trình giải mã DES cũng tương tự quá trình mã hóa. Chỉ khác là sẽ khác các khóa. Thay vì là từ 1 --> 16 thì giờ sẽ ngược lại và là 16 --> 1
![image](https://hackmd.io/_uploads/H1MgZkI5p.png)

## Double DES and Meet in the middle
### Double DES
-   DoubleDES (hay còn gọi là 2DES) là một thuật toán mã hóa đối xứng sử dụng khối được xây dựng trên cơ sở của DES. DoubleDES sử dụng hai khóa $Key_1$ và $Key_2$ để thực hiện mã hóa và giải mã dữ liệu, mỗi khóa có độ dài 56 bit.
-   Thuật toán DoubleDES thực hiện việc mã hóa bằng cách sử dụng hai giai đoạn mã hóa DES theo thứ tự liên tiếp.  Vì vậy, DoubleDES có thể được biểu diễn bằng công thức:
    $$Ciphertext = E(Key_2, E(Key_1, Plaintext))$$ $$Plaintext = D(Key_1 ,D(Key_2, Ciphertext))$$
-   Trong đó, plaintext là dữ liệu cần được mã hóa, $E(K_1, Plaintext)$ là kết quả sau khi dữ liệu được mã hóa với khóa $K_1$, và $E(K_2, E(K_1, Plaintext))$ là kết quả cuối cùng sau khi dữ liệu đã được mã hóa hai lần với hai khóa $K_1$ và $K_2$.
- Việc sử dụng 2 lần DES khiến thời gian bruteforce của nó trở nên rất lâu cụ thể là $2^{56}2^{56} = 2^{112}$.
- Tuy nhiên ta có thể rút ngắn thời gian bruteforce bằng cách sử dụng meet in the middle.
### Meet in the middle
- “Meet-in-the-middle” là một kỹ thuật tấn công được sử dụng để giảm đáng kể số lượng khóa có thể phải thử khi tấn công một hệ mã hóa. Đây là một phương pháp tấn công hiệu quả đối với các hệ mã hóa sử dụng khối mã hóa với khóa ngắn.
![image](https://hackmd.io/_uploads/S1vIwJI96.png)
- $M=EK_1(P)\ và\ M=DK_2(C)$
- Mã hóa P bằng cách sử dụng tất cả các giá trị có thể có của $K_1$ và ghi lại tất cả các giá trị thu được cho M.
- Giải mã C bằng cách sử dụng tất cả các giá trị có thể có của $K_2$ và ghi lại tất cả các giá trị thu được cho M.
- Tạo hai bảng được sắp xếp theo giá trị M.
- Bây giờ so sánh các giá trị cho M cho đến khi chúng ta tìm thấy các cặp đó $K_1,K_2$ mà giá trị của M giống nhau trong cả hai bảng
- Khi đó thay vì sử dụng $2^112$ lần để bruteforce, thì ta chỉ phải sử dụng $2^56$.
- Nếu chuyển từ DES-> 2DES thì ta cần bruteforce $2^57$.
## Triple DES
### Introduct
- 3DES hay Triple DES là một phiên bản được cải tiến của thuật toán mã hóa DES ban đầu cung cấp độ bảo mật cải thiện bằng cách sử dụng nhiều vòng mã hóa và độ dài khóa dài hơn. 3DES là một thuật toán mã hóa đối xứng, có nghĩa là cùng một khóa được sử dụng cho cả mã hóa và giải mã.
- Thuật toán 3DES sử dụng một nhóm khóa bao gồm 03 khóa DES K1, K2 và K3, mỗi khóa có giá trị 56 bits.
### Cơ chế hoạt động
![image](https://hackmd.io/_uploads/S1NQsQIcT.png)
**Mã hóa:**
- Trước tiên, thực hiện `encrypt` DES với khóa $K_1$, tiếp tục `decrypt` DES với khóa $K_2$ và cuối cùng `encrypt` DES với khóa $K_3$.
$$Ciphertext= E_{K3}(D_{K2}(E_{K1}(Plaintext))).$$

**Giải mã:**
- Đầu tiên, thực hiện `decrypt` DES với khóa $K_3$, tiếp tục `encrypt` DES với khóa $K_2$ và cuối cùng là `decrypt` DES với khóa $K_1$.
$$Ciphertext= D_{K1}(E_{K2}(D_{K3}(Ciphertext))).$$

**Key option:**
- Key option 1:
    - $K_1 \ne K_2 \ne K_3.$
    - Đây là option mạnh nhất với $3.56= 168$ bits độc lập. Tuy có thể bị bruteforce nhưng sẽ tốn khá nhiều thời gian với $2^{2.56}$ bước.
- Key option 2:
    - $K_1 \ne K_2$ và $K_1= K_3.$
    - Đây có thể coi là cải tiến của 2DES. Tuy nhiên vẫn không an toàn.
- Key option 3:
    - $K_1=\ K_2=\ K_3.$
    - Điều này tương đương với việc mã hóa DES 1 lần.
# PKCS#7 Padding
- Padding được sử dụng trong một số chế độ mật mã khối nhất định (như ECB và CBC) khi văn bản thuần túy cần phải là bội số của kích thước khối. Nếu chúng ta đang sử dụng mật mã khối 16 byte, nhưng văn bản thuần túy của chúng ta chỉ là 9 byte, thì chúng ta cần đệm dữ liệu của mình với 7 byte bổ sung.
- Để làm điều này, chúng tôi nối thêm 7 byte tất cả với giá trị của . Trường hợp chung là nếu chúng ta cần thêm N byte để tạo một khối đầy đủ, chúng ta nối thêm N byte, mỗi byte có giá trị là N. Điều này chỉ hoạt động nếu kích thước khối nhỏ hơn 256 byte, vì một byte chỉ có thể là một giá trị từ 0 đến 255.
- Ví dụ:
![image](https://hackmd.io/_uploads/H1OAn1I96.png)
- Khi giải mã, quá trình giải mã được thực hiện bằng cách xóa các byte đệm thêm vào cuối cùng của khối cuối cùng. Giá trị của byte cuối cùng được sử dụng để xác định số lượng byte đệm cần phải xóa.
# Advanced Encryption Standard- AES
## Introduct
- Trong mật mã học, Advanced Encryption Standard( nghĩa là tiêu chuẩn mã hóa tiên tiến) là một thuật toán mã hóa khối.
- Khác với DES- sử dụng mạng Feistel, AES sử dụng mạng thay thế- hoán vị.
- Không giống như DES, số vòng trong AES có thể thay đổi và phụ thuộc vào độ dài của khóa. AES sử dụng 10 vòng cho các phím 128 bit, 12 vòng cho các phím 192 bit và 14 vòng cho các phím 256 bit. Mỗi vòng này sử dụng một khóa tròn 128 bit khác nhau, được tính từ khóa AES ban đầu.
- Sơ đồ cấu trúc của AES được miêu tả như sau:
![image](https://hackmd.io/_uploads/H16oARv9a.png)
## Mã hóa
**Tổng quan:**
- AES sẽ lấy khối dữ liệu 128 bits từ plaintext thành 16 bytes để xếp thành ma trận 4x4.
- 1.Khởi động vòng lặp
    - AddRoundKey — Mỗi cột của trạng thái đầu tiên lần lượt được kết hợp với một khóa con theo thứ tự từ đầu dãy khóa.
- 2.Vòng lặp
    - SubBytes — đây là phép thế (phi tuyến) trong đó mỗi byte trong trạng thái sẽ được thế bằng một byte khác theo bảng tra (Rijndael S-box).
    - ShiftRows — dịch chuyển, các hàng trong trạng thái được dịch vòng theo số bước khác nhau.
    - MixColumns — quá trình trộn làm việc theo các cột trong khối theo một phép biến đổi tuyến tính.
    - AddRoundKey
- 3.Vòng lặp cuối
	- SubBytes
	- ShiftRows
	- AddRoundKey
- Tại chu trình cuối thì bước MixColumns không thực hiện.

**Chi tiết:**
- AES sẽ lấy khối dữ liệu 128 bits từ plaintext thành 16 bytes để xếp thành ma trận 4x4.
![image](https://hackmd.io/_uploads/Skuh-1_cp.png)
- Quá trình mã hóa của một vòng gồm 4 quy trình SubBytes, ShiftRows, MixColumns, AddRoundKey.
![image](https://hackmd.io/_uploads/B11Vkyd9T.png)
    - SubBytes: 16 bytes đầu vào được thay thế bằng cách tra cứu một bảng cố định (hộp S) được đưa ra trong thiết kế.
![image](https://hackmd.io/_uploads/BJclGJdc6.png)
- Đây là S-box của AES:
![image](https://hackmd.io/_uploads/rJsbUJuca.png)
    - Shiftrows:
        - Mỗi hàng trong số bốn hàng của ma trận được chuyển sang trái. Bất kỳ mục nào 'rơi ra' sẽ được chèn lại ở phía bên phải của hàng.
        - Hàng đầu tiên không bị dịch chuyển.
        - Hàng thứ hai được dịch chuyển một (byte) vị trí sang trái.
        - Hàng thứ ba được chuyển hai vị trí sang trái.
    	- Hàng thứ tư được chuyển ba vị trí sang trái.
    	- Kết quả là một ma trận mới bao gồm 16 byte giống nhau nhưng được dịch chuyển đối với nhau.
![image](https://hackmd.io/_uploads/rk8kQJOq6.png)
    - MixColumns: Bước này về cơ bản là phép nhân ma trận. Mỗi cột được nhân với một ma trận cụ thể và do đó vị trí của mỗi byte trong cột được thay đổi. Bước này được bỏ qua ở vòng cuối cùng.
![image](https://hackmd.io/_uploads/S1e_Ikdqp.png)
        - Ví dụ:
![image](https://hackmd.io/_uploads/rkrgo6ucp.png)
    - Addroundkey: Trong thao tác AddRoundKey, 128 bit của ma trận state sẽ được XOR với 128 bit của khóa con của từng vòng. Vì sử dụng phép XOR nên phép biến đổi ngược của AddRoundKey trong cấu trúc giải mã cũng chính là AddRoundKey. Việc kết hợp với khóa bí mật tạo ra tính làm rối (confusion) của mã hóa. Sự phức tạp của thao tác mở rộng khóa (KeySchedule) giúp gia tăng tính làm rối này.
    
    ![image](https://hackmd.io/_uploads/HkldnaOqp.png)
    


