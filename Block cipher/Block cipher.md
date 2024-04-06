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
## Giải mã
- Quá trình giải mã của một bản mã AES tương tự như quá trình mã hóa theo thứ tự ngược lại. Mỗi vòng bao gồm bốn quy trình được tiến hành theo thứ tự ngược lại:
    - AddRoundKey.
    - Inverse MixColumns.
    - ShiftRows.
    - Inverse SubBytes.
    
![image](https://hackmd.io/_uploads/ry4vRT_qT.png)
- Vì các quy trình phụ trong mỗi vòng diễn ra theo cách ngược lại, không giống như Feistel Cipher, các thuật toán mã hóa và giải mã cần được triển khai riêng biệt, mặc dù chúng có liên quan rất chặt chẽ.
    - Inverse MixColumns: thực hiện tương tự như MixColumns trong mã hóa, nhưng khác ở ma trận được sử dụng để thực hiện thao tác.
    - Inverse SubBytes: tương tự SubBytes.
# Block cipher modes of operation:
## Electronic Code Book- ECB
- ECB là chế độ hoạt động đơn giản nhất: Ta chia plaintext ra thành từng khối, mỗi khối có độ dài bằng 64 bit (hay độ dài quy định của block cipher), và thực hiện mã hóa độc lập từng khối.
- ECB có thể mã hóa song song các khối bit, do đó đây là một cách mã hóa nhanh hơn. Tuy nhiên lại dễ bị phân tích mật mã vì có mối quan hệ trực tiếp giữa bản rõ và bản mã
![image](https://hackmd.io/_uploads/SypWfCdqp.png)
![image](https://hackmd.io/_uploads/rJb-80u5p.png)
## Cipher Block Chaining- CBC
- Trong CBC, khối mật mã trước đó được đưa ra làm đầu vào cho thuật toán mã hóa tiếp theo sau XOR với khối văn bản rõ ban đầu.
- Encrypt: 
$$C_i = E_K(P_i ⊕ C_i - 1);\ C_0 = IV$$
![image](https://hackmd.io/_uploads/BkU1HR_9a.png)
- Decrypt:
$$P_{i}=D_{K}(C_{i})\oplus C_{i-1};\ C_{0}=IV$$
![image](https://hackmd.io/_uploads/Byi6IRO9a.png)
## Propagating cipher block chaining- PCBC
- Với PCBC mỗi khối bản rõ được XORed với cả khối văn bản thuần trước đó và khối bản mã trước đó trước khi được mã hóa. Giống như với chế độ CBC, một vectơ khởi tạo được sử dụng trong khối đầu tiên. Không giống như CBC, giải mã PCBC với IV (vectơ khởi tạo) không chính xác khiến tất cả các khối văn bản rõ bị hỏng.
- Encrypt:
$$C_i= E_k(P_i \oplus P_{i-1} \oplus P_{i-1}),\ P_0 \oplus C_0= IV$$
![image](https://hackmd.io/_uploads/rkKoiCOca.png)
- Decrypt:
$$P_i= D_k(C_i) \oplus P_{i-1} \oplus C_{i-1},\ P_0 \oplus C_0= IV$$
![image](https://hackmd.io/_uploads/Hk6CnROc6.png)
## Cipher Feedback- CFB
- Cipher Feedback (CFB) là một mode của thuật toán mã hóa block (block cipher) trong mật mã học. CFB hoạt động bằng cách sử dụng output của block cipher như một số liệu vào cho việc mã hóa dữ liệu tiếp theo, thay vì sử dụng trực tiếp khóa để mã hóa dữ liệu đó.
- Trong chế độ CFB, các khối plaintext sẽ được chia nhỏ thành các khối con và mỗi khối con này sẽ được mã hóa riêng bằng block cipher. Để thực hiện mã hóa, CFB sử dụng một vector khởi tạo (initialization vector - IV) để bắt đầu quá trình mã hóa. Kết quả của quá trình mã hóa sẽ được XOR với khối plaintext để tạo ra khối ciphertext tương ứng. Sau đó, khối ciphertext này sẽ được sử dụng làm đầu vào cho việc mã hóa khối tiếp theo.
- Encrypt:
$$\begin{cases}C_i= IV\\
C_i= E_K(C_{i-1}) \oplus P_i
\end{cases}$$
![image](https://hackmd.io/_uploads/S1FaZJY9T.png)
- Decrypt:
$$P_i= E_K(C_{i-1}) \oplus C_i$$
![image](https://hackmd.io/_uploads/Sk5kNyFcp.png)
## Output feedback- OFB
- OFB là một phương pháp điều khiển tự động trong đó đầu ra của hệ thống được sử dụng để điều khiển hệ thống. OFB là một phương pháp phổ biến để điều khiển các hệ thống có đầu vào không thể truy cập trực tiếp, chẳng hạn như các hệ thống có nhiều đầu vào hoặc các hệ thống có đầu vào không ổn định.
- Trong OFB, một bộ điều khiển được thiết kế để tạo ra một tín hiệu điều khiển sao cho đầu ra của hệ thống đạt được mục tiêu mong muốn. Tín hiệu điều khiển được tạo ra bằng cách tính toán sai số giữa đầu ra thực tế của hệ thống và đầu ra mong muốn. Sai số này được gọi là tín hiệu phản hồi.
- Phản hồi đầu ra có một số ưu điểm so với các phương pháp điều khiển khác. OFB có thể được sử dụng để điều khiển các hệ thống có đầu vào không thể truy cập trực tiếp. OFB cũng có thể được sử dụng để điều khiển các hệ thống có đầu vào không ổn định. Ngoài ra, OFB có thể được sử dụng để điều khiển các hệ thống có nhiều đầu vào.
- Do tính đối xứng của hoạt động XOR, mã hóa và giải mã hoàn toàn giống nhau:
$$C_j= P_j \oplus M_j$$ $$P_j= C_j \oplus O_j$$ $$O_j= E_K(I_j)$$ $$I_j= O_{j- 1}$$ $$I_0= IV$$
![image](https://hackmd.io/_uploads/B1ge_JF9p.png)
## Counter- CRT
- CTR (CM) còn được gọi là chế độ truy cập số nguyên (ICM) và segmented integer counter (SIC) mode.
- CTR là một phương pháp sử dụng block cipher để mã hóa dữ liệu theo các khối có kích thước cố định, tương tự như CBC và CFB. Tuy nhiên, CTR sử dụng một chuỗi giá trị đếm (counter) để tạo ra các key stream (khối mã hóa) để mã hóa các khối dữ liệu, thay vì sử dụng kết quả của các khối dữ liệu trước đó như CFB hoặc CBC.
![image](https://hackmd.io/_uploads/B1xP91Y56.png)

https://node-security.com/posts/cryptography-pkcs-7-padding/
https://viblo.asia/p/encryption-des-Qpmleq27lrd
https://isolution.pro/vi/t/cryptography/feistel-block-cipher/mat-ma-khoi-feistel
https://nguyenquanicd.blogspot.com/2019/09/aes-bai-1-ly-thuyet-ve-ma-hoa-aes-128.html    


