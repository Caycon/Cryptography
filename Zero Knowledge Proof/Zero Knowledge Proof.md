# Zero Knowledge Proof
## ZKP là gì?
- **ZKP** hay **Zero Knowledge Proof** là một phương pháp chứng minh cho bên xác thực rằng bản thân biết một thông tin bí mật nào đó nhưng lại không tiết lộ thông tin đó ra.
- Ví dụ kinh điển minh họa cho ZKP là Câu chuyện hang động **Hamiltonian**:
    - Giả sử bạn biết mật khẩu để mở một cánh cửa bí mật trong một hang động hình vòng tròn. Bạn muốn chứng minh với một người khác rằng bạn biết mật khẩu mà không tiết lộ mật khẩu thực sự.
    - Bạn bước vào hang động từ lối vào A hoặc B, và người xác minh đứng bên ngoài và không thể thấy bạn đi vào từ lối nào.
    - Sau đó, người xác minh yêu cầu bạn đi ra từ lối A hoặc B (tùy chọn). Nếu bạn thực sự biết mật khẩu, bạn có thể đi ra từ lối mà họ yêu cầu bằng cách đi qua cánh cửa. Nếu bạn không biết mật khẩu, xác suất để bạn đoán đúng lối ra sẽ chỉ là 50%.
    - Bằng cách lặp lại quá trình này nhiều lần, người xác minh sẽ dần tin rằng bạn thực sự biết mật khẩu mà không cần phải tiết lộ nó.
![image](https://github.com/user-attachments/assets/e2d9d294-4e5f-4422-a452-6a3226da5748)
- Một số ZKP thường thấy như:
    - **Interactive ZKP:**
        - **Sigma protocol.**
    - **Non-interactive ZKP:**
        - **ZK-SNARK:** Zero-Knowledge Succinct Non-Interactive Argument of Knowledge.
        - **ZK-STARK:** Zero-Knowledge Scalable Transparent Argument of Knowledge.

| Loại ZKP | Tính tương tác | Kích thước bằng chứng | Thời gian xác minh | Giả định về tính toán | Ứng dụng điển hình |
|---|---|---|---|---|---|
| **ZK-SNARK** | Không tương tác | Nhỏ gọn | Nhanh | Có (giả định về hàm băm) | Blockchain, xác thực danh tính |
| **ZK-STARK** | Không tương tác | Lớn hơn SNARK | Chậm hơn SNARK | Không có | Blockchain, xác thực tính toàn vẹn dữ liệu |
| **Sigma protocol** | Tương tác | Trung bình | Trung bình | Không có | Nền tảng cho các ZKP phức tạp hơn |
## Cách thức hoạt động
- **ZKP** hoạt động dựa trên một giao thức mật mã đặc biệt, cho phép một bên (người chứng minh) thuyết phục bên còn lại (người xác minh) về tính đúng đắn của một tuyên bố mà không cần tiết lộ bất kỳ thông tin cụ thể nào.
- Nguyên tắc hoạt động chung của ZKP:
    - Tạo một câu đố: Người chứng minh tạo ra một câu đố toán học phức tạp liên quan đến thông tin mà họ muốn chứng minh.
    - Giải câu đố: Người chứng minh giải câu đố và chứng minh rằng họ có giải pháp.
    - Xác minh: Người xác minh kiểm tra xem lời giải của người chứng minh có đúng hay không, nhưng không cần biết chi tiết về cách giải.

| Ưu điểm của ZKP | Nhược điểm của ZKP |
|---|---|
| **Bảo mật cao:** Bảo vệ thông tin cá nhân và dữ liệu nhạy cảm hiệu quả. | **Độ phức tạp:** Các thuật toán ZKP thường rất phức tạp và khó triển khai. |
| **Quyền riêng tư:** Cho phép xác thực thông tin mà không tiết lộ dữ liệu gốc. | **Hiệu năng:** Việc tạo và xác minh bằng chứng ZKP có thể tiêu tốn nhiều tài nguyên tính toán. |
| **Tăng cường tin tưởng:** Tạo sự tin tưởng giữa các bên tham gia giao dịch. | **Tính tương thích:** Khó tích hợp ZKP vào các hệ thống hiện có. |
| **Khả năng mở rộng:** Có thể sử dụng để mở rộng quy mô của các hệ thống blockchain. | **Tiêu chuẩn hóa:** Chưa có tiêu chuẩn chung cho ZKP. |
| **Ứng dụng đa dạng:** Có thể áp dụng trong nhiều lĩnh vực khác nhau. | **Mối đe dọa an ninh:** Có thể bị tấn công nếu không được thiết kế và triển khai đúng cách. |
## Ứng dụng
- **Blockchain và tiền điện tử:**
    - Giao dịch ẩn danh: ZKP cho phép thực hiện các giao dịch trên blockchain mà không tiết lộ thông tin về người gửi và người nhận, bảo vệ quyền riêng tư.
    - Xác minh tuổi: ZKP có thể được sử dụng để xác minh tuổi của người dùng mà không cần tiết lộ ngày sinh cụ thể.
    - Mở rộng quy mô: Các giải pháp ZK-Rollups sử dụng ZKP để tăng khả năng xử lý giao dịch của blockchain, giảm phí giao dịch và cải thiện hiệu suất.
- **Xác thực danh tính:**
    - Đăng nhập không mật khẩu: ZKP cho phép người dùng đăng nhập vào các dịch vụ trực tuyến mà không cần nhập mật khẩu, tăng cường bảo mật.
    - Xác minh tài liệu: ZKP có thể được sử dụng để xác minh tính xác thực của các tài liệu như bằng lái xe, hộ chiếu mà không cần chia sẻ toàn bộ thông tin.
- **Bảo mật dữ liệu doanh nghiệp:**
    - Kiểm toán dữ liệu: ZKP có thể được sử dụng để kiểm toán dữ liệu mà không cần truy cập trực tiếp vào dữ liệu gốc, đảm bảo tính bảo mật và riêng tư.
    - Bảo vệ tài sản trí tuệ: ZKP có thể được sử dụng để chứng minh quyền sở hữu đối với các tài sản trí tuệ mà không cần tiết lộ chi tiết về tài sản đó.

## Practice
### SNARK
- Cho $xy+4= 10$. Ta sẽ chứng minh rằng ta biết các giá trị $x;y$.
![image](https://github.com/user-attachments/assets/2036be49-8285-4a1e-b414-4e4b563a8850)
$$output_1= xy\ (1)$$
$$output_2= output_1 +4= 10\ (2)$$
- Ta lập được vector sau:
$$<L,v>*<R,v>= <O,v>$$
$$v= [1;x;y;output_1]$$
- Với $(1)$:
$$L= [0;1;0;0]\ (x) \\ R= [0;0;1;0]\ (y)\\ O= [0;0;0;1]\ (output_1)$$ 
- Với $(2)$:
$$L= [4;0;0;1]\ (output_1 + 5)$$
$$R= [1;0;0;0]$$
$$O= [10;0;0;0]$$ 
- Dựng đa thức với Lagrange interpolation([QAP](https://www.rareskills.io/post/quadratic-arithmetic-program)):
$$L_1(x)= 4x-4\\ L_2(x)=-x+2\\ L_3(x)= 0\\ L_4(x)= x-1$$
- Ta có $P = L(x) * R(x) - O(x) = T(x) * H(x)$
- Trong đó $T(x)$ được public để xác minh, $H(x)$ được người chứng minh cung cấp.
- Người chứng minh sẽ tính toán các giá trị của các đa thức L(x), R(x), O(x) và H(x) tại một điểm x nào đó và gửi các giá trị này cho người xác minh.
- Người xác minh sẽ kiểm tra xem phương trình trên có đúng hay không với các giá trị đã nhận được.

### Obscure Evaluation
#### Homomorphic Encryption
- **Homomorphic Encryption** cho phép mã hóa một giá trị có thể áp dụng các phép toán vào mã hóa.
- Có nhiều cách để đạt được các thuộc tính `Homomorphic` của mã hóa. Ví dụ:
    - Ở đây ta chọn 1 số tự nhiên là $7$ làm cơ số để mã hóa một số khác bằng cách lũy thừa. Ở đây mình lấy $4$ là số cần mã hóa. Thực tế thì có thể chọn nhiều cách mã hóa khác phức tạp hơn.
    - Ta có: $$7^4= 2401$$ 
    - Nếu ta lũy thừa thêm lần nữa (bên xác minh yêu cầu để xem ta có biết bí mật thực sự là gì hay không và so sánh kết quả khi lũy thừa thêm lần nữa có trùng khớp kết quả hay không). Ở đây tôi lũy thừa thêm cho $$4$: 
    $$2401^4= 33232930569601$$
    - Tuy nhiên thì cơ số là phần public nên rất dễ để có thể tìm ra số bí mật khi ta xác minh như trên dù ta không trực tiếp nói ra số bí mật để xác minh.

#### Modular Arithmetic
- Phần này thì mng hãy tưởng tượng số bí mật của mng là một số lớn hơn rất nhiều so với modulo mà các bạn xét.
- Giả dụ như số bí mật của các bạn là $407$, modulo của bạn là $47$.
$$407 \equiv 31 mod(47)$$
- Lúc này vì không biết kích thước của số bí mật nên ta sẽ thu được 1 tập gồm các số có dạng số bí mật:
$$47k+ 31$$
- Từ đó ta có thể sử dụng zkp ở đây. Ta có thể yêu cầu người nắm bí mật cho ta biết kết quả khi ta nhân hay cộng trừ hoặc thực hiện 1 phép toán nào đó để xác minh xem người đó có thực sự nắm bí mật đó không. Tất nhiên nếu ta xác minh nhiều lần thì phải sử dụng nhiều thuận toán hay phép toán khác nhau để trang người khác tìm được quy luật của thuật toán.

#### Strong Homomorphic Encryption
- Tương tự **Homomorphic Encryption** nhưng ta kết hợp thêm modulo. Lúc này việc tìm được số bí mật trở nên khó hơn rất nhiều do có nhiều số có cùng tính chất với số bí mật

#### Encrypted Polynomial
- Xét $$p(x)= x^3- 3x^2+2x$$
- Dựa vào **homomorphic encryption** ta không được phép lũy thừa trực tiếp, ta sẽ sử dụng các giá trị của các lũy thừa của x đã má hóa sẵn như $E(x), E(x^2), E(x^3)$ Điều này cho phép chúng ta tính toán đa thức đã mã hóa một cách gián tiếp.
- Ví dụ, ta có thể tính toán giá trị mã hóa của đa thức như sau:
$$E(x^3).E(x^2)^{-3}E(x)^2$$
- Suy ra:
$$(g^{x^3})(g^{x^2})^{-3}(g^{x^2})$$
$$g^{x^3-3x^2+2x}$$
- Kết quả này là giá trị đã mã hóa của đa thức $p(x)$ với x không được biết.
- Xét một cách tổng quát ta có:
> Verifier:
    >- Lấy một giá trị ngẫu nhiên $s$ bí mật.
    >- Tính toán các giá trị mã hóa của $s$ cho các lũy thừa từ $s^0$ đến $s^d$, tức $E(s^i)= g^{s^i}$.
    >- Tính giá trị của đã thức địch $t(s) dưới dạng chưa mã hóa.
    >- Cung cấp cho **Prover** các giá trị đã mã hóa của các lũy thừa $s$: $E(s^0), E(s^1),..., E(s^d)$.

> Prover
    >- Tính $h(x)= \frac{p(x)}{t(x)}$.
    >- Sử dụng các giá trị đã mã hóa của $s$ để tính $E(p(s))$ và $E(h(s))$ với các hệ số $c_0, c_1,...c_n$.
    >- Gửi $g^p$ và $g^h$.