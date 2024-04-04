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
### CRT
- `CRT` hay `Chinese Remainder Theorem` chính là thặng dư Trung Hoa, dựa vào thuật toán này, kỹ thuật `CRT` được hình thành.
- `CRT` là kỹ thuật thường được sử dụng trong quá trình `decrypt` để tối ưu hóa việc tính toán.
- Thông thường ta sẽ dùng công thức sau để giải mã:
$$M \equiv C^d\ mod(N)$$
- Tuy nhiên thay vì tính $M$ bằng cách thực hiện lên toàn bộ công thức, CRT cho phép chia nhỏ nó thành các phần nhỏ hơn để tăng tốc quá trình giải mã. Cụ thể, CRT chia $d$ thành $d_p,\ d_q$,  tương ứng với các thành phần liên quan đến phép tính modulo $p$ và $q$.
$$M_p \equiv C^{d_p}\ mod(p)$$ $$M_q \equiv C^{d_q}\ mod(q)$$
- Sau đó, CRT được sử dụng để kết hợp $M_p,\ M_q$ ta sẽ thu được $M$.
### Common modulus
**External Attack:**
- Kiểu tấn công này thường được áp dụng trong kịch bản có  1 plantext nhưng lại sử dụng 2 hay nhiều Public key khác nhau $(N, e_1);(N, e_2)$. Tương ứng ta cũng sẽ có $C_1, C_2$.
- Thường thì đối với kịch bản này họ sẽ cung cấp cho ta giá trị của $(C_1,e_1, N),  (C_2, e_2, N) $ với điều kiện $d(e_1, e_2)= 1$.
- Với $d(e_1, e_2)= 1$ thì sẽ tồn tại cặp (a, b) thỏa mãn:
$$ae_1+ be_2= 1$$  $$\text{(Extended Euclidean Algorithm)}$$.
- Khi đó ta có: 
$$C_1^aC_2^b= m^{ae_1}m^{be_2} = m^{ae_1 + be_2} = m$$.
- Nếu $d(e_1, e_2)= x.\ Với\ x \ne 1$ thì tương tự cũng sẽ tồn tại cặp (a, b) thỏa mãn:
$$ae_1+ be_2= x$$  $$\text{(Extended Euclidean Algorithm)}$$.
- Tiếp tục ta sẽ có:
$$C_1^aC_2^b= m^{ae_1}m^{be_2} = m^{ae_1 + be_2} = m^ x$$ $$=> m= \sqrt[x]{C_1^aC_2^b}$$.
**Internal attack**
- Ta được biết là: 
$$de= 1 mod(\phi(n))$$ $$<=> de= k\phi(n) +1$$ $$<=> k= \frac{de- 1}{\phi(n)}(1)$$
- Trong kịch bản bạn là một thành viên trong nhóm và được sở hữu (n, e, d) của riêng bản thân bạn.
- Dựa vào (1) ta có thể tính được k dựa trên việc $\phi(n) \approx n$ để tìm k từ đó suy ra $\phi(n)$.
- Khi đó:
$$\begin{cases}
k= \frac{de- 1}{n}+ x(x \in \mathbb{N^*})\\
\phi(n)= \frac{ed- 1}{k}
\end{cases}$$
- Ta sẽ tăng x lên cho đến khi nào tìm được $\phi(n)$ thỏa mãn.
- Khi có được $\phi(n)$ ta có thể dễ dàng lấy được thông tin của các cá nhân khác nếu họ để lộ $e$ của họ.
## Demo
- Ở đây ta có một số challenge của giải ctf:
### RSA101 
[Link](https://github.com/Caycon/RSA/blob/main/RSA_101.zip)
**Challenge 0: Outer_tower**
- Challenge chỉ cung cấp cho ta $(c,\ e)$ và cho phép ta gửi plantext bất kỳ để encrypt với n của flag. Lưu ý $n=\ p$.
- Với challenge này thì tôi có ý tưởng như sau:
- Ta có:
$$c \equiv m^c\ mod(p)$$
- Đặt:
$$c_2 \equiv 2^e\ mod(p)$$ $$c_3 \equiv 3^e\ mod(p)$$ $$c_4 \equiv 4^e\ mod(p)$$ $$c_6 \equiv 6^e\ mod(p)$$ $$=> \begin{cases} c_2c_2- c_4=\ k_4n\ (k_4 \in \mathbb{N^*})\\
c_2c_3-c_6=\ k_6n\ (k_6 \in \mathbb{N^*})
\end{cases}$$ $$=> gcd(c_2c_2- c_4, c_2c_3-c_6)=  (a \in \mathbb{N^*})$$
```Python
from Crypto.Util.number import *
import sage
from factordb.factordb import FactorDB
c2= 91290982576242698078301355426160297874699598235585104763497506856109507746447756164018082201650501583791185997527237426280420863107809914695883586595240168716667470198566863594513391484954454858778632223864493060900623246970462839923303676707669928375270900202153763541838488063003250682626330645215513933107
c3= 127178409289562366711431696987160820204248234750700658785267661714592604024211476064488763376192171619420072088131176213844904194083896986637768015109419816803275815134816983564937239963527249885280904013972033001993773344652863721338119062918114208660076679186133900445480812331084865769556960991291804028960
c4= 30859130945619809630556579026275518424614763878784123184420612220620907240779222173495653996046624908642602071167890870269438841541977226356457414223511202723378846654661984891014710884887366201979464737154914040756478926168997534319918723733065568697534556377883594445767565694821072457118624638532656270161
c6= 61050081989711817988472919184351705824194348417199848443026198522228096398381186876533867812095604025174557780777490672817126614994634347102186995399940226652418686193892349978642010395812512397767529133979185885682993141692079378673275285645951900166140604230657991523223955480509927846704921720215430395220
e= 65537
a= c2*c2-c4
b= c2*c3- c6
x= GCD(a, b)
f = FactorDB(x)
f.connect()
t= f.get_factor_list()
p = max(t)
d= inverse(e, p- 1)
c= 15664280369288029576575049830939618031655108939747106497837420984704705351920987198520803542631769861813292942997882236690922788922261682366085816589227942250103740248334448701566930972063541791395979600363242451063852041494730426596487048373029333659066169243105670286292975339587566892590804378767576287235
print(long_to_bytes(pow(c, d, p)))
```
![image](https://hackmd.io/_uploads/Hk84AtOFa.png)
**Challenge 1: Flour_of_test**
- Challenge này ta có ý tưởng sẽ sử dụng `CRT` do e nhỏ và ta có nhiều giá trị (n, c) tương ứng.
- Sử dụng `Hastad Attack` ta thu được flag.
![image](https://hackmd.io/_uploads/HJscOFdKa.png)

**Challenge 2: The_Workshop_Battle**
- Challenge này sử dụng kỹ thuật `Blinding`:
$$r^e mod(N)$$
- Với $r$ là `admin` tuy nhiên lại không cho phép ta gửi `admin` vào. Nhưng ta hoàn toàn có thể gửi vào bằng cách phân tích 'admin' thành 2 số $160658^*2603647$ và lần lượt gửi chúng vào dưới dạng hex.
$$(admin)^e\ mod(n)$$ $$= (160658)^e(2603647)^e\ mod(n)$$
![image](https://hackmd.io/_uploads/S1NUN2uKT.png)

**Challenge 3: Hell_train**
- Challenge này thoạt nhìn thì ta thấy rằng đây chỉ là RSA thông thường với n không thể phân tích trong thời gian ngắn, tuy nhiên nếu đọc kỹ ta sẽ tìm được cách thức tạo n.
![image](https://hackmd.io/_uploads/SkWqHtDcp.png)

- $n= pq$ trong đó $p= 2(x^a)+ 1$ với x là số nguyên tố a là số nguyên thuộc khoảng từ 45-> 50. Đây là đặc điểm của n sau khi tôi phân tích cách tạo p.

*Solve:*
```Python
from Crypto.Util.number import*
import sage
n = 3304723233832088793922393934181960094288040618680647960110512377142017056359018458627089830847262559791894497373232794205602632842781489839326316146794565122189652925418199158338751005616192360457528777281780202639182931538174822962760799908080826692915134130612654279984958746833380070194853714478071171415046894569370667637379706498399
e = 65537
c = 3171565737715551170817627747564480885978328159434643145636534204549889585340944216709470344384514460092374671912986952442262004832774179262963755573492850093763425853500157066850822681867726707078328565704423214096538780283154684472941623075000888661588080225207138541704460814848252447690346815259125571720011853434577916667349839750776
