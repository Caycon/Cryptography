# Cryptography
- `Cryptography` hay mật mã học là một ngành khoa học nghiên cứu về việc mã hóa và giải mã thông tin. Mục đích của mật mã học là bảo vệ thông tin khỏi những kẻ tấn công, những người có thể muốn đọc hoặc thay đổi thông tin đó.

- Mật mã học có thể được sử dụng để bảo vệ nhiều loại thông tin, bao gồm:

    - Thông tin cá nhân, chẳng hạn như số thẻ tín dụng, số an sinh xã hội và mật khẩu
    - Thông tin kinh doanh, chẳng hạn như bí mật thương mại và thông tin tài chính
    - Thông tin nhạy cảm, chẳng hạn như thông tin quân sự và tình báo
    - Mật mã học sử dụng các thuật toán toán học để biến thông tin thông thường thành dạng không thể đọc được. Chỉ những người có khóa giải mã phù hợp mới có thể giải mã thông tin đã được mã hóa.
- Các đặc điểm chính của mật mã học bao gồm:
    - Tính bảo mật: Mật mã học được thiết kế để bảo vệ thông tin khỏi những kẻ tấn công.
    - Tính toàn vẹn: Mật mã học có thể được sử dụng để xác minh rằng thông tin không bị thay đổi trong quá trình truyền tải.
    - Tính xác thực: Mật mã học có thể được sử dụng để xác minh danh tính của người gửi thông tin.
# Cryptanalysis
- `Cryptanalysis` là quá trình phân tích các mật mã và hệ thống mật mã để phá vỡ chúng và truy cập thông tin đã được mã hóa mà không có khóa bí mật. Nó là một lĩnh vực nghiên cứu quan trọng trong mật mã học, vì nó giúp đảm bảo rằng các hệ thống mật mã là an toàn và bảo mật.
- Mục tiêu của phân tích mật mã là:
    - Tìm ra khóa bí mật: Đây là mục tiêu cao nhất của phân tích mật mã, vì nó sẽ cho phép kẻ tấn công giải mã tất cả thông tin được mã hóa bằng thuật toán đó.
    - Trích xuất thông tin một phần: Ngay cả khi kẻ tấn công không thể tìm ra khóa bí mật, họ vẫn có thể trích xuất thông tin hữu ích từ thông tin đã được mã hóa. Ví dụ: họ có thể xác định người gửi hoặc người nhận thông điệp, hoặc họ có thể xác định chủ đề của thông điệp.
    - Tìm ra cách giải mã thay thế: Trong một số trường hợp hiếm hoi, kẻ tấn công có thể tìm ra cách giải mã thông tin đã được mã hóa mà không cần khóa bí mật. Điều này thường xảy ra khi thuật toán mã hóa có lỗi hoặc khi kẻ tấn công có quyền truy cập vào thông tin bổ sung về thuật toán hoặc hệ thống.
# Encode/Decode
- `Encode/Decode` là quá trình chuyển đổi thông tin từ dạng ban đầu sang dạng khác, thường là để bảo mật thông tin.
- `Encode` là quá trình mã hóa, là quá trình chuyển đổi thông tin từ dạng ban đầu, có thể đọc được thành dạng không thể đọc được, thường được gọi là bản mã. Quá trình mã hóa sử dụng một khóa, là một chuỗi ký tự hoặc số được sử dụng để mã hóa và giải mã thông tin.
- `Decode` là quá trình giải mã, là quá trình chuyển đổi thông tin từ dạng không thể đọc được, thường được gọi là bản mã, trở lại dạng ban đầu, có thể đọc được. Quá trình giải mã cũng sử dụng khóa giống như quá trình mã hóa.
- Các đặc điểm của encode/decode bao gồm:
    - Tính bảo mật: Encode/decode được sử dụng để bảo vệ thông tin khỏi những kẻ tấn công. Bằng cách mã hóa thông tin, chỉ những người có khóa mới có thể giải mã và đọc được thông tin đó.
    - Tính toàn vẹn: Encode/decode cũng có thể được sử dụng để xác minh tính toàn vẹn của thông tin. Nếu thông tin đã được mã hóa và giải mã thành công, thì nó có thể được đảm bảo là không bị thay đổi trong quá trình truyền tải.
    - Tính xác thực: Encode/decode cũng có thể được sử dụng để xác minh danh tính của người gửi thông tin. Ví dụ, chữ ký điện tử sử dụng encode/decode để xác minh rằng thông tin đã được gửi bởi người cụ thể mà nó tuyên bố được gửi bởi.
- Một số kỹ thuật encode/decode phổ biến bao gồm:
    - Mã hóa đối xứng: Sử dụng cùng một khóa để mã hóa và giải mã thông tin.
    - Mã hóa bất đối xứng: Sử dụng hai khóa riêng biệt, một khóa để mã hóa và một khóa khác để giải mã thông tin.
    - Mã hóa dựa trên hàm băm: Sử dụng hàm băm để tạo một bản tóm tắt của thông tin, sau đó được mã hóa bằng một khóa.
- Encode/decode là một lĩnh vực quan trọng trong mật mã học. Nó được sử dụng trong nhiều ứng dụng khác nhau để bảo vệ thông tin khỏi những kẻ tấn công.
# Encrypt/Decrypt
- `Encrypt` là quá trình chuyển đổi thông tin từ dạng có thể đọc được thành dạng không thể đọc được, thường được gọi là bản mã. Quá trình mã hóa sử dụng một khóa, là một chuỗi ký tự hoặc số được sử dụng để mã hóa và giải mã thông tin. 
- `Decrypt` là quá trình chuyển đổi thông tin từ dạng không thể đọc được, thường được gọi là bản mã, trở lại dạng ban đầu, có thể đọc được. Quá trình giải mã cũng sử dụng khóa giống như quá trình mã hóa. 
![image](https://hackmd.io/_uploads/r1xq8Ua_6.png)
- Các đặc điểm của mã hóa/giải mã bao gồm:
    - Tính bảo mật: Mã hóa được sử dụng để bảo vệ thông tin khỏi những kẻ tấn công. Bằng cách mã hóa thông tin, chỉ những người có khóa mới có thể giải mã và đọc được thông tin đó.
    - Tính toàn vẹn: Mã hóa cũng có thể được sử dụng để xác minh tính toàn vẹn của thông tin. Nếu thông tin đã được mã hóa và giải mã thành công, thì nó có thể được đảm bảo là không bị thay đổi trong quá trình truyền tải.
    - Tính xác thực: Mã hóa cũng có thể được sử dụng để xác minh danh tính của người gửi thông tin. Ví dụ, chữ ký điện tử sử dụng mã hóa/giải mã để xác minh rằng thông tin đã được gửi bởi người cụ thể mà nó tuyên bố được gửi bởi.
- Điểm khác biệt giữa `Encode/Decode` và `Encrypt/Decrypt`:
![image](https://hackmd.io/_uploads/B1-euUada.png)
    - Encrypt/Decrypt:
        - Mã hóa mật khẩu trước khi lưu trữ trong cơ sở dữ liệu.
        - Bảo vệ thông tin thẻ tín dụng trong quá trình giao dịch trực tuyến.
        - Mã hóa email để đảm bảo tính bảo mật.
    - Encode/Decode:
        - Nén tệp để giảm kích thước và tiết kiệm dung lượng lưu trữ (ví dụ: nén ZIP).
        - Chuyển đổi hình ảnh sang định dạng JPEG hoặc PNG để hiển thị trên web.
        - Chuyển đổi văn bản sang mã ASCII để truyền qua mạng.
# Symmetric and Asymmetric Cryptography
- `Symmetric and Asymmetric Cryptography` hay `mã hóa đối xứng` và `mã hóa bất đối xứng` là hai loại mã hóa chính được sử dụng để bảo vệ thông tin. Cả hai loại mã hóa đều sử dụng khóa để mã hóa và giải mã thông tin, nhưng chúng khác nhau về cách thức sử dụng khóa.
## Symmetric Cryptography
- Mã hóa đối xứng sử dụng cùng một khóa để mã hóa và giải mã thông tin. Khóa này được chia sẻ giữa người gửi và người nhận. Mã hóa đối xứng thường được sử dụng cho các ứng dụng yêu cầu tốc độ cao, chẳng hạn như mã hóa dữ liệu lưu trữ hoặc mã hóa kết nối mạng. Vd: `AES (Advanced Encryption Standard)`, `DES (Data Encryption Standard)`,...
- Đặc điểm:
    - Khóa: Mã hóa đối xứng sử dụng cùng một khóa để mã hóa và giải mã thông tin. Khóa này được chia sẻ giữa người gửi và người nhận.
    - Tính bảo mật: Tính bảo mật của mã hóa đối xứng phụ thuộc vào độ dài của khóa. Khóa càng dài thì càng khó để bẻ khóa.
    - Tốc độ: Mã hóa đối xứng thường nhanh hơn mã hóa bất đối xứng. Điều này là do mã hóa đối xứng chỉ cần sử dụng một khóa, trong khi mã hóa bất đối xứng cần sử dụng hai khóa.
    - Ứng dụng: Mã hóa đối xứng thường được sử dụng cho các ứng dụng yêu cầu tốc độ cao, chẳng hạn như mã hóa dữ liệu lưu trữ hoặc mã hóa kết nối mạng.
    - Ưu điểm:
        - Tốc độ nhanh.
        - Dễ triển khai.
        - Yêu cầu phần cứng và phần mềm đơn giản.
    - Nhược điểm:
        - Tính bảo mật thấp hơn mã hóa bất đối xứng.
        - Yêu cầu chia sẻ khóa giữa người gửi và người nhận.
## Asymmetric Cryptography
- Mã hóa bất đối xứng sử dụng hai khóa khác nhau, một khóa công khai và một khóa riêng tư. Khóa công khai được chia sẻ với mọi người, trong khi khóa riêng tư được giữ bí mật bởi người sở hữu. Mã hóa bất đối xứng thường được sử dụng cho các ứng dụng yêu cầu tính bảo mật cao, chẳng hạn như xác thực và ký điện tử. Vd: `RSA (Rivest–Shamir–Adleman)`,...
- Đặc điểm:
    - Khóa: Mã hóa bất đối xứng sử dụng hai khóa khác nhau, một khóa công khai và một khóa riêng tư. Khóa công khai được chia sẻ với mọi người, trong khi khóa riêng tư được giữ bí mật bởi người sở hữu.
    - Tính bảo mật: Tính bảo mật của mã hóa bất đối xứng phụ thuộc vào độ phức tạp của thuật toán mã hóa và độ dài của khóa. Khóa càng dài và thuật toán mã hóa càng phức tạp thì càng khó để bẻ khóa.
    - Tốc độ: Mã hóa bất đối xứng thường chậm hơn mã hóa đối xứng. Điều này là do mã hóa bất đối xứng cần sử dụng hai khóa, trong khi mã hóa đối xứng chỉ cần sử dụng một khóa.
    - Ứng dụng: Mã hóa bất đối xứng thường được sử dụng cho các ứng dụng yêu cầu tính bảo mật cao, chẳng hạn như xác thực và ký điện tử.
    - Ưu điểm:
        - Tính bảo mật cao.
        - Không cần chia sẻ khóa.
        - Có thể sử dụng cho các ứng dụng yêu cầu xác thực và ký điện tử.
    - Nhược điểm:
        - Tốc độ chậm.
        - Yêu cầu phần cứng và phần mềm mạnh mẽ hơn.
- Lựa chọn loại mã hóa phù hợp phụ thuộc vào các yêu cầu cụ thể của ứng dụng. Nếu tốc độ là quan trọng, thì mã hóa đối xứng là lựa chọn tốt hơn. Nếu tính bảo mật là quan trọng, thì mã hóa bất đối xứng là lựa chọn tốt hơn.
## Điểm khác biệt:
|**Symmetric Key Encryption** | **Asymmetric Key Encryption** |
|---|---|
| Chỉ yêu cầu một khóa duy nhất cho cả mã hóa và giải mã. | Yêu cầu hai khóa, khóa công khai và khóa riêng, một khóa để mã hóa và khóa còn lại để giải mã.|
| Kích thước của văn bản mật mã bằng hoặc nhỏ hơn văn bản thuần túy gốc. | Kích thước của văn bản mật mã bằng hoặc nhỏ hơn văn bản thuần túy gốc. |
| Quá trình mã hóa nhanh. | Quá trình mã hóa chậm. |
| Được sử dụng khi một lượng lớn dữ liệu được yêu cầu để chuyển. | Được sử dụng để chuyển một lượng nhỏ dữ liệu. |
| Cung cấp tính bảo mật. | Cung cấp tính bảo mật, tính xác thực và không thoái thác. |
| Độ dài của khóa được sử dụng là 128 hoặc 256 bit. | Độ dài của khóa được sử dụng là 2048 hoặc cao hơn. |
| Ít tốn tài nguyên hơn. | Tốn nhiều tài nguyên hơn. |
| Xử lý lượng lớn dữ liệu. | Xử lý một lượng nhỏ dữ liệu. |
| Bảo mật ít hơn vì chỉ có một khóa được sử dụng cho cả mục đích mã hóa và giải mã. | An toàn hơn vì hai khóa được sử dụng ở đây - một để mã hóa và một để giải mã. |
# Block Cipher and Stream Cipher
## Block Cipher
- `Block cipher` là thuật toán mã hóa chia nhỏ dữ liệu thành các khối cố định kích thước và mã hóa từng khối một. Kích thước khối thường là 64 hoặc 128 bit.
- Đặc điểm của block cipher:
    - Cách thức mã hóa dữ liệu: Block cipher chia dữ liệu thành các khối cố định kích thước, thường là 64 hoặc 128 bit. Mỗi khối được mã hóa độc lập với các khối khác.
    - Kích thước khối: Kích thước khối là một thông số quan trọng của thuật toán block cipher. Kích thước khối càng lớn thì khả năng kháng lại tấn công bằng lực brute càng cao. Tuy nhiên, kích thước khối lớn cũng làm giảm tốc độ mã hóa.
    - Tốc độ: Block cipher thường chậm hơn stream cipher. Điều này là do block cipher cần xử lý từng khối dữ liệu một, trong khi stream cipher có thể mã hóa từng bit dữ liệu một.
    - Ứng dụng: Block cipher thường được sử dụng cho các ứng dụng yêu cầu tính bảo mật cao, chẳng hạn như mã hóa dữ liệu lưu trữ và truyền tải.
- Các bước mã hóa dữ liệu bằng block cipher:
    - Chia dữ liệu thành các khối cố định kích thước.
    - Sử dụng khóa để mã hóa từng khối dữ liệu.
    - Ghép các khối dữ liệu đã được mã hóa lại với nhau để tạo thành bản mã.
- Các bước giải mã dữ liệu bằng block cipher:
    - Chia bản mã thành các khối cố định kích thước.
    - Sử dụng khóa để giải mã từng khối dữ liệu.
    - Ghép các khối dữ liệu đã được giải mã lại với nhau để tạo thành bản rõ.
- Một số thuật toán block cipher phổ biến:
    - AES (Advanced Encryption Standard).
    - DES (Data Encryption Standard).
    - 3DES.
    - Blowfish.
    - Twofish.
    - Serpent.
- Ưu điểm của block cipher:
    - Tính bảo mật cao.
    - Có thể chống lại các tấn công bằng brute.
    - Có thể được sử dụng cho các ứng dụng yêu cầu tính bảo mật cao.
- Nhược điểm của block cipher:
    - Tốc độ chậm hơn `stream cipher`.
    - Yêu cầu phần cứng và phần mềm mạnh mẽ.
## Stream Cipher
- `Stream cipher` là một thuật toán mã hóa chuyển đổi dữ liệu thành một luồng bit và mã hóa từng bit một. 
- Đặc điểm của stream cipher:
    - Cách thức mã hóa dữ liệu: Stream cipher chuyển đổi dữ liệu thành một luồng bit, sau đó mã hóa từng bit một.
    - Kích thước khối: Kích thước khối của stream cipher không giới hạn.
    - Tốc độ: Stream cipher thường nhanh hơn block cipher. Điều này là do stream cipher có thể mã hóa từng bit dữ liệu một, trong khi block cipher cần xử lý từng khối dữ liệu một.
    - Ứng dụng: Stream cipher thường được sử dụng cho các ứng dụng yêu cầu tốc độ cao, chẳng hạn như mã hóa dữ liệu truyền tải.
- Các bước mã hóa dữ liệu bằng stream cipher:
    - Chuyển đổi dữ liệu thành một luồng bit.
    - Sử dụng khóa để mã hóa từng bit dữ liệu.
    - Ghép các bit dữ liệu đã được mã hóa lại với nhau để tạo thành bản mã.
- Các bước giải mã dữ liệu bằng stream cipher:
    - Chuyển đổi bản mã thành một luồng bit.
    - Sử dụng khóa để giải mã từng bit dữ liệu.
    - Ghép các bit dữ liệu đã được giải mã lại với nhau để tạo thành bản rõ.
- Một số thuật toán stream cipher phổ biến:
    - RC4.
    - ChaCha20.
    - Salsa20.
- Ưu điểm của stream cipher:
    - Tốc độ nhanh.
    - Yêu cầu phần cứng và phần mềm đơn giản hơn.
    - Có thể được sử dụng cho các ứng dụng yêu cầu tốc độ cao.
- Nhược điểm của stream cipher:
    - Tính bảo mật thấp hơn block cipher.
    - Có thể bị tấn công bằng phương pháp phân tích tần số.
    - Có thể bị tấn công bằng phương pháp phân tích tấn công khóa liên quan.
## Điểm khác biệt
| **Đặc điểm** | **Block Cipher** | **Stream Cipher** |
|---|---|---|
| **Chuyển đổi** | Chuyển đổi từng khối văn bản | Chuyển đổi từng byte văn bản |
| **Kích thước khối** | 64 bit hoặc hơn | 8 bit |
| **Độ phức tạp** | Đơn giản | Phức tạp hơn |
| **Kỹ thuật sử dụng** | Cả hoán vị (confusion) và phân tán (diffusion) | Chỉ sử dụng hoán vị |
| **Độ khó giải mã văn bản đã mã hóa** | Khó | Dễ |
| **Chế độ thuật toán** | ECB (Electronic Code Book) và CBC (Cipher Block Chaining) | CFB (Cipher Feedback) và OFB (Output Feedback) |
| **Kỹ thuật mã hóa** | Kỹ thuật hoán vị như rail-fence, columnar transposition | Kỹ thuật thay thế như Caesar cipher, polygram substitution |
| **Tốc độ** | Chậm hơn stream cipher | Nhanh hơn block cipher |
| **Ứng dụng** | Lưu trữ tệp, truyền thông internet | Lưu trữ tệp, truyền thông internet |
| **Bảo mật khi sử dụng khóa nhiều lần** | An toàn hơn stream cipher | Ít an toàn hơn block cipher |
| **Độ dài khóa** | Thường là 128 hoặc 256 bit | Thường là 128 hoặc 256 bit |
| **Cách thức hoạt động** | Mã hóa trên các khối dữ liệu có kích thước cố định | Mã hóa từng bit hoặc byte dữ liệu một |
# Hash Function
- `Hash Function` hay hàm băm là một hàm toán học biến đầu vào có kích thước, độ dài bất kỳ thành đầu ra tiêu chuẩn có độ dài nhất định. Giá trị đầu ra của hàm băm được gọi là giá trị băm, mã băm, thông điệp băm, hoặc đơn giản là hash.
- Các đặc điểm của hàm băm bao gồm:
    - Tính một chiều: Giá trị băm của một đầu vào không thể suy ra được đầu vào ban đầu.
    - Tính không trùng lặp: Hai đầu vào khác nhau sẽ có giá trị băm khác nhau.
    - Tính phân tán: Giá trị băm của một đầu vào có thể được sử dụng để phân loại các đầu vào khác nhau vào các nhóm có liên quan.
- Một số hàm băm phổ biến bao gồm:
    - MD5: Một hàm băm 128 bit được sử dụng rộng rãi trong nhiều ứng dụng, bao gồm xác thực mật khẩu và kiểm tra tính toàn vẹn của dữ liệu.
    - SHA-1: Một hàm băm 160 bit được sử dụng trong nhiều ứng dụng, bao gồm mã hóa dữ liệu và xác thực nguồn gốc của dữ liệu.
    - SHA-256: Một hàm băm 256 bit được sử dụng trong nhiều ứng dụng, bao gồm mã hóa dữ liệu và xác thực nguồn gốc của dữ liệu.
- Đây là một ví dụ về `hash function`:
    - Plaintext: `The power of cryptography`.
    - MD5: `bf3e25942f42920e1151638ded6d2aca`.
    - SHA256: `006af56e49da317e5c4ac673920b84e189deee62a641591462576ab07bbcbcf5`
