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
