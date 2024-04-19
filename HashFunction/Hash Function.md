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
>- Secure Hashing Algorithm 2 (SHA-2):
    - Là một trong những họ hàm băm phổ biến và được sử dụng nhiều nhất hiện nay.
    - Xuất bản năm 2001 với các kích thước đầu ra $224, 256, 384$ hoặc $512$ bits.
    - SHA-2 sử dụng cấu trúc Merkle-Damgård để nén dữ liệu thành một chuỗi ngắn hơn.
    - Cấu trúc Merkle-Damgård sử dụng các bước:
    - Bổ sung bắt buộc (Mandatory Padding): Thêm một chuỗi đặc biệt và chiều dài của tin nhắn vào cuối tin nhắn để đảm bảo kích thước đạt bội số của khối dữ liệu.
    - Nén (Compression): Xử lý từng khối dữ liệu theo thứ tự, sử dụng hàm nén để tạo ra giá trị trung gian.
    - Đầu ra (Output): Giá trị băm cuối cùng là kết quả của công đoạn nén cuối.
- Keccak: Hàm băm Keccak là победитель (pobeditel - tiếng Nga) của cuộc thi NIST tổ chức để tìm ra hàm băm cho Secure Hashing Algorithm 3 (SHA-3).
- Keccak sử dụng cấu trúc sponge với hai giai đoạn: hấp thụ (absorbing) và chiết xuất (squeezing).
- SHA-3 gồm các phiên bản: SHA3–224, SHA3–256, SHA3–384, SHA3–512, SHAKE128, và SHAKE256. Đặc biệt, SHAKE có thể tạo ra giá trị băm với kích thước tùy ý.

## Tích chất- Đặc điểm
- Hàm băm mật mã có 6 tính chất sau:
    - Tính xác định — Deterministic: cùng một chuỗi đầu vào, hàm băm luôn trả về một kết quả giống nhau.
    - Nhanh chóng — Quick: tiêu tốn ít thời gian để tính toán giá trị băm của bất kì chuỗi đầu vào nào.
    - Hàm một chiều — One-way function: không khả thi (không thể) để tìm được giá trị chuỗi đầu vào khi biết giá trị băm của nó trừ khi thử hết tất cả các giá trị có thể.
    - Hiệu ứng lan truyền — Avalanche effect: chỉ một sự thay đổi nhỏ của message có thể thay đổi đáng kể kết quả hash đến nỗi ta không biết được mối liên hệ với kết quả hash cũ.
    - Ngăn chặn đụng độ — Collision resistant: không khả thi (không thể) để tìm được giá trị 2 chuỗi đầu vào có cùng kết quả giá trị băm.
    - Ngăn chặn tấn công tiền ảnh — Pre-image attack resistant: Một cách tấn công vào các hàm băm mật mã thường cố tìm một message có giá trị hash đã cho trước. Các hàm băm mật mã phải chống lại được kiểu tấn công này.

## Attack hash function
**Collision attack:**
- Collision attack là một dạng tấn công trong mật mã học, kẻ tấn công cố gắng tìm hai đầu vào khác nhau tạo ra cùng một giá trị băm (hash value). Nói cách khác, họ muốn tìm hai thông điệp (message) $M_1$ và $M_2$ sao cho $H(M_1) = H(M_2)$, trong đó H là hàm băm.

- Mục đích của Collision attack:

    - Ký giả mạo chữ ký điện tử: Kẻ tấn công có thể tạo ra một văn bản giả mạo có cùng chữ ký điện tử với một văn bản hợp lệ khác, đánh lừa người nhận tin rằng văn bản giả mạo là do người gửi hợp pháp tạo ra.
    - Thay đổi nội dung tin nhắn: Kẻ tấn công có thể thay đổi nội dung tin nhắn đã được ký và xác thực, sau đó tạo ra một chữ ký mới cho tin nhắn đã sửa đổi, khiến người nhận tin tin rằng tin nhắn vẫn là bản gốc.
    - Phá mã xác thực tin nhắn (MAC): Kẻ tấn công có thể tạo ra hai tin nhắn khác nhau nhưng có cùng giá trị MAC, khiến hệ thống xác thực tin nhắn tin rằng hai tin nhắn này là giống nhau.
- Loại Collision attack:

    - Collision attack cổ điển: Kẻ tấn công không có bất kỳ thông tin gì về hàm băm hay các đầu vào trước đây. Họ chỉ sử dụng các phương pháp toán học và thử nghiệm để có thể collision attack.
    - Collision attack được hỗ trợ trước: Kẻ tấn công có một số thông tin về hàm băm hoặc các đầu vào trước đây, giúp họ dễ dàng tìm kiếm các giấ trị cần kiếm hơn.
    - Collision attack có chọn lọc: Kẻ tấn công có thể chọn một đầu vào cụ thể $(M_1)$ và tìm kiếm đầu vào thứ hai $(M_2)$ để $H(M_1) = H(M_2)$.
- Tham khảo thêm tại [Collision attack](https://en.wikipedia.org/wiki/Collision_attack).

**Preimage attack:**
- Preimage attack: là một dạng tấn công mật mã học trong đó kẻ tấn công cố gắng tìm một giá trị đầu vào (preimage) cụ thể tạo ra một giá trị băm (hash value) đã được biết. Nói cách khác, kẻ tấn công biết giá trị băm H(x) và muốn tìm x sao cho H(x) = H(y), trong đó y là giá trị băm đã biết.

- Mục đích của tấn công tiền ảnh:

    - Ký giả mạo chữ ký điện tử: Kẻ tấn công có thể giả mạo chữ ký điện tử của một người khác bằng cách tìm ra giá trị đầu vào tạo ra cùng giá trị băm với chữ ký hợp lệ.
    - Phá mã xác thực tin nhắn (MAC): Kẻ tấn công có thể thay đổi nội dung tin nhắn đã được ký và xác thực, sau đó tạo ra một giá trị MAC mới cho tin nhắn đã sửa đổi, khiến người nhận tin tin rằng tin nhắn vẫn là bản gốc.
    - Khôi phục mật khẩu: Kẻ tấn công có thể sử dụng giá trị băm của mật khẩu được lưu trữ để giải mã mật khẩu.
- Tham khảo thêm tại [Preimage attack](https://en.wikipedia.org/wiki/Preimage_attack).

**Birthday attack:**
- Birthday attack là một kỹ thuật tấn công mật mã học dựa trên xác suất để tìm kiếm hai giá trị đầu vào tạo ra cùng một giá trị băm. Nói cách khác, kẻ tấn công cố gắng tìm hai thông điệp $M_1$ và $M_2$ sao cho $H(M_1) = H(M_2)$, trong đó H là hàm băm.

- Mục đích của Birthday attack:

    - Ký giả mạo chữ ký điện tử: Kẻ tấn công có thể tạo ra một văn bản giả mạo có cùng chữ ký điện tử với một văn bản hợp lệ khác, đánh lừa người nhận tin rằng văn bản giả mạo là do người gửi hợp pháp tạo ra.
    - Phá mã xác thực tin nhắn (MAC): Kẻ tấn công có thể tạo ra hai tin nhắn khác nhau nhưng có cùng giá trị MAC, khiến hệ thống xác thực tin nhắn tin rằng hai tin nhắn này là giống nhau.
    - Thay đổi nội dung tin nhắn: Kẻ tấn công có thể thay đổi nội dung tin nhắn đã được ký và xác thực, sau đó tạo ra một chữ ký mới cho tin nhắn đã sửa đổi, khiến người nhận tin tin rằng tin nhắn vẫn là bản gốc.
- Nguyên lý hoạt động:

    - Birthday attack dựa trên xác suất thống kê. Với một nhóm ít nhất $23$ người, xác suất để có ít nhất hai người có cùng ngày sinh nhật là hơn $50%$. Tương tự, với một hàm băm có $n$ giá trị đầu vào khả thi, xác suất để tìm kiếm hai đầu vào tạo ra cùng một giá trị băm sau $\sqrt{n}$ phép tính là khoảng $50%$.

- Ví dụ:

    - Với hàm băm MD5 có $2^{128}$ giá trị đầu vào khả thi, kẻ tấn công có thể tìm kiếm va chạm sau khoảng $2^{64}$ phép tính (tương đương với $1.85$ x $10^{19}$ phép tính).
    - Với hàm băm SHA-256 có $2^{256}$ giá trị đầu vào khả thi, kẻ tấn công cần khoảng $2^{128}$ phép tính (tương đương với $3.40$ x $10^{38}$ phép tính) để tìm kiếm va chạm.
- So sánh với tấn công va chạm:

    - Birthday attack không yêu cầu kẻ tấn công có bất kỳ thông tin gì về hàm băm hay các đầu vào trước đây.
    - Birthday attack thường hiệu quả hơn tấn công va chạm cổ điển, đặc biệt là với các hàm băm có độ dài đầu ra ngắn.
    - Tuy nhiên, Birthday attack vẫn tốn kém tài nguyên tính toán hơn so với một số loại tấn công va chạm khác như tấn công va chạm được hỗ trợ trước.
- Tham khảo thêm tại đây [Birthday attack](https://en.wikipedia.org/wiki/Birthday_attack)
- [Length extension attack](https://www.bing.com/search?q=length+extension+attack&cvid=848b20e29b7d4056a65183b771c6db8c&gs_lcrp=EgZjaHJvbWUqBggBEAAYQDIGCAAQRRg5MgYIARAAGEAyBggCEAAYQDIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMgYIBxAAGEAyBggIEAAYQNIBCDkxMTdqMGo5qAIFsAIB&FORM=ANAB01&PC=ACTS)
