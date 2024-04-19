# Hash Function
## Introduct
- `Hàm băm(hash function)`: là một phép toán chuyển một chuỗi ký tự đầu vào (có độ dài bất kỳ) thành một chuỗi đầu ra có độ dài cố định. Bài viết phân loại hàm băm thành 3 loại chính:
    - `Hàm băm mật mã`: Được dùng trong chữ ký điện tử và mã xác thực tin nhắn (MAC). Loại hàm này cần đáp ứng các yêu cầu về khả năng kháng tiền ảnh (preimage resistance), kháng va chạm thứ hai (second preimage resistance) và kháng va chạm (collision resistance) đồng thời có kết quả đầu ra giả ngẫu nhiên (pseudo-random output).
    - `Hàm băm không mật mã`: Được dùng trong bảng băm (hash table) của ngôn ngữ lập trình và phát hiện lỗi như kiểm tra dư thừa tuần hoàn (CRC) và thuật toán Adler-32. Loại hàm này không cung cấp bảo mật.
    - `Hàm băm gần đúng (fuzzy hash function)`: Là hàm nén dùng để tính toán mức độ tương đồng giữa hai đầu vào. Loại hàm này cho phép sai số và có thể dùng để xác định sự khác biệt giữa hai đầu vào dựa trên mã băm của chúng. Ứng dụng bao gồm phân loại phần mềm độc hại và giám định pháp y kỹ thuật số. SSDEEP là một ví dụ về hàm băm gần đúng.
>- Các yêu cầu cần thiết cho một hàm băm mật mã trước khi đi vào chi tiết về loại hàm này. Các yêu cầu bao gồm:
    - `Khả năng kháng tiền ảnh (preimage resistance)`: Cho một giá trị hash đầu ra h, bất khả thi tìm được một input y nào tạo ra giá trị hash h. Nghĩa là, không thể nào dựa vào kết quả đầu ra (hash) để tìm lại dữ liệu ban đầu.
    - `Khả năng kháng va chạm thứ hai (second preimage resistance)`: Cho một input x, bất khả thi tìm được một input khác y (khác với x) tạo ra cùng giá trị hash với x. Nghĩa là, khó có thể tạo ra hai dữ liệu đầu vào khác nhau nhưng lại cho cùng một kết quả hash.
    - `Output giả ngẫu nhiên (output pseudo-randomness)`: Giá trị đầu ra của hàm băm phải trông giống như ngẫu nhiên, không có bất kỳ mô hình nào phân biệt được. Điều này đảm bảo tính khó đoán của giá trị hash.
- Hàm băm không nhất thiết phải tạo ra giá trị đầu ra duy nhất cho mỗi giá trị đầu vào. Điều này chỉ có thể xảy ra nếu hàm băm có đầu ra với độ dài vô hạn.
![image](https://hackmd.io/_uploads/HyXtz_IxC.png)
- Bản chất của việc ánh xạ từ không gian vô hạn (đầu vào) sang không gian hữu hạn (đầu ra) sẽ luôn dẫn đến va chạm (hai đầu vào khác nhau cho cùng một kết quả).
- Độ dài tin nhắn đầu vào có thể rất lớn. Ví dụ, SHA-256 chỉ chấp nhận tối đa $2^{64}$ bits, còn SHA-3 không giới hạn kích thước đầu vào.
- Giả sử giới hạn đầu vào là $1024$ bits (chỉ là một phần nhỏ của toàn bộ không gian đầu vào). SHA-256 cho ra giá trị băm $256$ bits, nghĩa là có tổng cộng $2^{256}$ giá trị băm khác nhau. Tuy nhiên, với $2^{1024}$ đầu vào thì trung bình sẽ có đến $2^{768}$ cặp đầu vào có cùng giá trị băm.
- Tuy nhiên, với các hàm băm mật mã bảo mật cao, việc tìm lại tin nhắn gốc từ giá trị băm hoặc tạo ra hai tin nhắn khác nhau có cùng giá trị băm là gần như bất khả thi.

>- Một số hàm băm tiêu biểu:
    - Message Digest 4 (MD4) (1990): Đầu ra $128$ bits.
    - MD5 (1992): Đầu ra $128$ bits.
    - RIPE MD (RIPEMD) (1992): Đầu ra $128, 160, 256$ và $320$ bits.
    - Secure Hash Algorithm 1 (SHA-1) (1995): Đầu ra $160$ bits.
    - Whirlpool (2000): Đầu ra $512$ bits.
- Lưu ý về tính bảo mật:

    - Một số hàm băm trong danh sách đã được biết đến các lỗ hổng bảo mật, có thể tạo ra va chạm (hai đầu vào khác nhau cho cùng một kết quả).
    - Do đó, không nên sử dụng MD4, MD5 và SHA-1 cho các ứng dụng đòi hỏi tính bảo mật cao. RIPEMD với kích thước đầu ra lớn, Whirlpool và SHA-1 vẫn được sử dụng trong một số thuật toán khác.
