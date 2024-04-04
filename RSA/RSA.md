# RSA
## Introduction
**Khái niệm:**
- Theo `wikipedia` thì RSA trong mật mã học mang khái niệm như sau: RSA là một thuật toán mật mã hóa khóa công khai. Đây là thuật toán đầu tiên phù hợp với việc tạo ra chữ ký điện tử đồng thời với việc mã hóa. Nó đánh dấu một sự tiến bộ vượt bậc của lĩnh vực mật mã học trong việc sử dụng khóa công cộng. RSA đang được sử dụng phổ biến trong thương mại điện tử và được cho là đảm bảo an toàn với điều kiện độ dài khóa đủ lớn.
- RSA là một thuật toán mã hóa bất đối xứng, nó sử dụng hai khóa riêng biệt để mã hóa và giải mã dữ liệu. Khóa công khai được chia sẻ với công chúng, trong khi khóa bí mật được giữ bí mật.

**Cách hoạt động:**
- Chọn Số Nguyên Tố:
    - Chọn hai số nguyên tố lớn ngẫu nhiên, đặt chúng là p và q.
    - Tính $n = pq$. n là một số nguyên dương lớn và được sử dụng làm phần công khai của khóa.
- Tính Hàm Euler:
    - Tính hàm Euler của n, ký hiệu là $φ(n)$. Đối với $n = pq$, $φ(n)= (p-1)(q-1)$.
- Chọn Số E:
    - Chọn một số nguyên dương e sao cho 1 < e < φ(n) và d(e, φ(n))= 1. Số e được chọn làm phần công khai của khóa.
- Tính Số D:
    - Tìm số nguyên d sao cho $de= 1 mod(φ(n))$. Số d được chọn làm phần bí mật của khóa.
- Tạo Khóa Công Khai và Bí Mật:
    - Khóa công khai là cặp (n, e).
    - Khóa bí mật là cặp (n, d).
- Mã Hóa và Giải Mã:
    - Mã hóa: Tìm c số nguyên dương c từ m thông qua công thức $c ≡ m^e (mod\ n)$.
    - Giải mã: Tìm m từ c thông qua công thức $m ≡ c^d (mod\ n)$.
**Demo:**
- Chọn số nguyên tố:
    - Ta chọn (p, q)= (229, 281).
    - $n= pq= 64349$
- Tính φ(n):
    - $φ(n)= (p-1)(q-1)$.
- Chọn e thỏa mãn $d(e, φ)= 1$. Ta chọn e= 17389.
- Mã hóa:
    - Ta chọn `plantext` là: `R54` hay chính là `m= 5387572`.
    - $c= m^e (mod n) <=> c= 32554$
- Dựa vào những thông tin trên ta có thể thiết kế một challenge như sau:
    - Tìm tên loại mật mã được ẩn giấu với các thông tin sau:
        ```Python
        e= 17389
        n= 64349
        c= 32554
        #c= pow(c, e, n)
        ```
    - Với challenge trên ta có thể nhìn ra thông điệp đã được mã hóa bằng `RSA`. Để tìm được thông điệp bị ẩn giấn ta cần có được khóa bí mật, ở trường hợp này ta cần có được `d` để tìm được thông điệp.
    - Ta có $d= e^{-1} (mod\ φ(n))\ với\ φ(n)= (p-1)(q-1)$.
    - Lúc này thông điệp của ta hay chính là m sẽ bằng: $m \equiv c^d (mod\ n)$
    - Ta có code giải mã như sau:
    ```Python
    from Crypto.Util.number import *
    # m= 5387572
    e= 17389
    n= 64349
    c= 32554
    p= 229
    q= 281
    phi= (p-1)*(q-1)
    d= pow(e, -1, phi)
    print(long_to_bytes(pow(c, d, n)))
    ```
    ![image](https://hackmd.io/_uploads/Bkdr7TMtT.png)
    - Tuy nhiên khi nhận được kết quả ta lại không thể đọc được thông điệp đó là gì do ta đã mắc sai lầm ở hàm `modulo` ta sẽ fix code để tìm ra thông điệp:
    ```Python
    from Crypto.Util.number import *
    # m= 5387572
    e= 17389
    n= 64349
    p= 229
    q= 281
    c= 32554
    phi= (p-1)*(q-1)
    d= pow(e, -1, phi)
    for i in range(1000):
        print(long_to_bytes(pow(c, d, n)+ i*n))
    ```
    - Tìm trong các kết quả được in ra ta thấy cụm từ `R54` xuất hiện và nó chính là loại mật mã cần tìm.

    ![image](https://hackmd.io/_uploads/H1oom6GKa.png)
## Attack RSA
### Factoring
- Với một số bài toán n không đủ lớn ta có thể phân tích được n để tìm khóa bí mật từ đó giải mã.
- Link phân tích n: [Factordb](http://www.factordb.com/), [alpertron](https://www.alpertron.com.ar/ECM.HTM).
### e small
- Với bài toán có số e đủ nhỏ ta có thể tính từ biểu thức $c \equiv m^e (mod\ n)$. Do n là số lớn hơn rất nhiều so với c, e nên $c= m^e + n*0 <=> c= m^e$.
- Bài toán này có thể có biến đổi đi 1 chút và cho $c= m^e+ n*k \text{ Với k} \in \mathbb{Z}$. Ta có thể nhận ra điều này bởi vì lúc này c sẽ lớn hơn n.
### Fermat's attack
-  Đây là phương pháp được sử dụng khi ta nhận định khóa `n` được tạo từ 2 số nguyên tố p, q gần bằng nhau.
- Khi đó ta có biểu thức sau(Ta sẽ xét p> q):
$$n= pq$$ $$<=>n= (\frac{p+q}{2})^ 2 (\frac{p-q}{2})^2$$(1)
- Đặt:
$$(2)\begin{cases}
x+y& = 5\\ 
x-y& = 3
\end{cases}$$
- Từ (1)(2) suy ra:
$$n= x^2+ y^2$$
- Tới đây ta sử dụng phương pháp [Fermat Factor](https://en.wikipedia.org/wiki/Fermat's_factorization_method) để tìm  p, q.
###  Hastad's broadcast Attack
- Với những bài toán RSA cho:
$$\begin{cases}
1\ e.\\
nhiều\ cặp\ (c, n)\ tương\ ứng.
\end{cases}$$
- Loại bài toán này khá giống với `small public`, thế nên dựa vào cơ sở của `small public` và định lý `Thặng dư Trung Hoa` để giải quyết.
- Tham khảo thêm [CopperSmith](https://en.wikipedia.org/wiki/Coppersmith%27s_attack)
### Blinding Attack
- Kỹ thuật `blinding` là một phương pháp được sử dụng trong hệ thống mật mã RSA để bảo vệ chống lại các cuộc tấn công dựa trên thông tin phản hồi từ quá trình giải mã. Mục tiêu chính của kỹ thuật này là ngăn chặn các tấn công kiểu side-channel attack, trong đó kẻ tấn công có thể sử dụng thông tin như thời gian thực hiện, công suất tiêu thụ điện năng, hoặc các dạng thông tin phản hồi khác để suy luận ra khóa bí mật.
- Trong hệ thống RSA, một số loại tấn công side-channel có thể tận dụng thông tin như thời gian giải mã, để suy luận ra khóa bí mật. Kỹ thuật blinding giúp ngăn chặn các loại tấn công này bằng cách thêm vào một yếu tố ngẫu nhiên vào quá trình giải mã. Yếu tố này được gọi là `blinding factor`.
- Quá trình giải mã RSA thông thường như sau:
    - Mã hóa: $C \equiv M^e mod(N)$
    - Giải mã: $M \equiv C^d mod(N)$
- Khi sử dụng kỹ thuật blinding, quá trình giải mã được thay đổi như sau:
    - Tạo một số ngẫu nhiên `r` và tính $r^e mod(N)$, được gọi là  `blinding factor`$(r< N, d(r, N)= 1)$.
    - Nhân $C$ với blinding factor: $C' \equiv Cr^e mod(N)$
    - Giải mã $C'$ thay vì $C$: $M' \equiv C'^d mod(N)$
    - Nhân $M'$ với $r^{-1} mod(N)$ để loại bỏ blinding factor: $M \equiv M'r^{-1} mod(N)$ 
- Một số phương pháp có thể tấn công được kỹ thuật 'Blinding' nếu nó không được triển khai cẩn thận:
    - `Implementation Fault Attacks`: Nếu quá trình triển khai blinding không được thực hiện đúng cách, kẻ tấn công có thể tận dụng những lỗ hổng này để lấy thông tin về khóa bí mật. Ví dụ, nếu có lỗi trong việc xác định và thực hiện blinding factor, thông tin có thể rò rỉ qua các kênh không mong muốn.
    - `Instruction Timing Attacks`: Kẻ tấn công có thể theo dõi thời gian thực hiện các lệnh trong quá trình giải mã. Nếu có sự biến đổi đáng kể trong thời gian thực hiện dựa trên giá trị của blinding factor, họ có thể sử dụng thông tin này để suy luận ra khóa bí mật.
    - `Power Analysis Attacks`: Kẻ tấn công có thể theo dõi mức tiêu thụ công suất của hệ thống trong quá trình giải mã. Nếu blinding factor không được thực hiện chính xác, các biến động trong công suất có thể tiết lộ thông tin về khóa bí mật.
    - `State-Based Attacks`: Kẻ tấn công có thể cố gắng suy luận giá trị của blinding factor hoặc các thông tin khác từ trạng thái nội tại của hệ thống. Nếu họ có thể đoán được giá trị của blinding factor, tấn công có thể trở nên hiệu quả hơn.
    - `Fault injection`: Kỹ thuật này bao gồm việc chèn lỗi (fault injection) vào hệ thống để làm suy giảm hiệu suất của blinding. Nếu blinding không hoạt động chính xác, thông tin về khóa bí mật có thể trở nên dễ thu được.
### CRT
- `CRT` hay `Chinese Remainder Theorem` chính là thặng dư Trung Hoa, dựa vào thuật toán này, kỹ thuật `CRT` được hình thành.
- `CRT` là kỹ thuật thường được sử dụng trong quá trình `decrypt` để tối ưu hóa việc tính toán.
- Thông thường ta sẽ dùng công thức sau để giải mã:
$$M \equiv C^d\ mod(N)$$
- Tuy nhiên thay vì tính $M$ bằng cách thực hiện lên toàn bộ công thức, CRT cho phép chia nhỏ nó thành các phần nhỏ hơn để tăng tốc quá trình giải mã. Cụ thể, CRT chia $d$ thành $d_p,\ d_q$,  tương ứng với các thành phần liên quan đến phép tính modulo $p$ và $q$.
$$M_p \equiv C^{d_p}\ mod(p)$$ $$M_q \equiv C^{d_q}\ mod(q)$$
- Sau đó, CRT được sử dụng để kết hợp $M_p,\ M_q$ ta sẽ thu được $M$.
