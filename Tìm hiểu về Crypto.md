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
