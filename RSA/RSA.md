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

### Wiener Attack
- Phương pháp này dựa trên việc d đủ nhỏ để tấn công:
$$d< \frac{1}{3}n^\frac{1}{4}$$
- Ta có thể nhận biết được d đủ nhỏ thông qua các yếu tố sau:
    - Bài toán cho điều kiện của $d< \frac{1}{3}n^\frac{1}{4}$.
    - Tỷ lệ của $\frac{e}{n}$
    - $\frac{1}{3}n^\frac{1}{4}$ nhỏ. Do $d< \frac{1}{3}n^\frac{1}{4}$.
    - e lớn.
- Cách hoạt động:
    - Ta có:
    $$ed \equiv 1 mod(\phi{(n)})$$ $$<=> ed= k\phi{(n)}\ (Với\ k \in \mathbb{Z})(1)$$ $$<=> \frac{e}{\phi{(n)}}= \frac{k}{d}+ \frac{1}{\phi{(n)}}(*)$$
    - Dựa vào (1) ta thấy rằng $ed \approx k \phi{(n)}$.
    - Mặt $\ne$:
    $$\begin{cases}
    \phi{(n)}= (p-1)(q-1)= n- p- q- 1\\
    p+ q- 1< \sqrt{n}
    \end{cases}$$
    - Từ đây ta suy ra:
    $$\frac{e}{n}- \frac{k}{d} \leq \frac{3k\sqrt{n}}{nd}$$ $$<=> \begin{cases} \frac{e}{\phi(n)}< 1\\ \frac{1}{d\phi(n)}< 1 \end{cases}$$ $$<=> \frac{k}{d}< 1$$ $$<=> d< k$$ $$=> \frac{e}{n}- \frac{k}{d}< \frac{1}{2d^2}$$.
    - Sử dụng dãy hội tụ của $\frac{e}{n}$ ta sẽ tìm được $\frac{k}{d}$.
    - Tham khảo thêm [Boneh Durfee Attack](https://www.sciencedirect.com/science/article/pii/S0304397518305371). Đây là một kỹ thuật nâng cao hơn so với `Wiener Attack`.

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
f= [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, 4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, 4153, 4157, 4159, 4177, 4201, 4211, 4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, 4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409, 4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, 4507, 4513, 4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, 4591, 4597, 4603, 4621, 4637, 4639, 4643, 4649, 4651, 4657, 4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729, 4733, 4751, 4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813, 4817, 4831, 4861, 4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937, 4943, 4951, 4957, 4967, 4969, 4973, 4987, 4993, 4999, 5003, 5009, 5011, 5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087, 5099, 5101, 5107, 5113, 5119, 5147, 5153, 5167, 5171, 5179, 5189, 5197, 5209, 5227, 5231, 5233, 5237, 5261, 5273, 5279, 5281, 5297, 5303, 5309, 5323, 5333, 5347, 5351, 5381, 5387, 5393, 5399, 5407, 5413, 5417, 5419, 5431, 5437, 5441, 5443, 5449, 5471, 5477, 5479, 5483, 5501, 5503, 5507, 5519, 5521, 5527, 5531, 5557, 5563, 5569, 5573, 5581, 5591, 5623, 5639, 5641, 5647, 5651, 5653, 5657, 5659, 5669, 5683, 5689, 5693, 5701, 5711, 5717, 5737, 5741, 5743, 5749, 5779, 5783, 5791, 5801, 5807, 5813, 5821, 5827, 5839, 5843, 5849, 5851, 5857, 5861, 5867, 5869, 5879, 5881, 5897, 5903, 5923, 5927, 5939, 5953, 5981, 5987, 6007, 6011, 6029, 6037, 6043, 6047, 6053, 6067, 6073, 6079, 6089, 6091, 6101, 6113, 6121, 6131, 6133, 6143, 6151, 6163, 6173, 6197, 6199, 6203, 6211, 6217, 6221, 6229, 6247, 6257, 6263, 6269, 6271, 6277, 6287, 6299, 6301, 6311, 6317, 6323, 6329, 6337, 6343, 6353, 6359, 6361, 6367, 6373, 6379, 6389, 6397, 6421, 6427, 6449, 6451, 6469, 6473, 6481, 6491, 6521, 6529, 6547, 6551, 6553, 6563, 6569, 6571, 6577, 6581, 6599, 6607, 6619, 6637, 6653, 6659, 6661, 6673, 6679, 6689, 6691, 6701, 6703, 6709, 6719, 6733, 6737, 6761, 6763, 6779, 6781, 6791, 6793, 6803, 6823, 6827, 6829, 6833, 6841, 6857, 6863, 6869, 6871, 6883, 6899, 6907, 6911, 6917, 6947, 6949, 6959, 6961, 6967, 6971, 6977, 6983, 6991, 6997, 7001, 7013, 7019, 7027, 7039, 7043, 7057, 7069, 7079, 7103, 7109, 7121, 7127, 7129, 7151, 7159, 7177, 7187, 7193, 7207, 7211, 7213, 7219, 7229, 7237, 7243, 7247, 7253, 7283, 7297, 7307, 7309, 7321, 7331, 7333, 7349, 7351, 7369, 7393, 7411, 7417, 7433, 7451, 7457, 7459, 7477, 7481, 7487, 7489, 7499, 7507, 7517, 7523, 7529, 7537, 7541, 7547, 7549, 7559, 7561, 7573, 7577, 7583, 7589, 7591, 7603, 7607, 7621, 7639, 7643, 7649, 7669, 7673, 7681, 7687, 7691, 7699, 7703, 7717, 7723, 7727, 7741, 7753, 7757, 7759, 7789, 7793, 7817, 7823, 7829, 7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919, 7927, 7933, 7937, 7949, 7951, 7963, 7993, 8009, 8011, 8017, 8039, 8053, 8059, 8069, 8081, 8087, 8089, 8093, 8101, 8111, 8117, 8123, 8147, 8161, 8167, 8171, 8179, 8191, 8209, 8219, 8221, 8231, 8233, 8237, 8243, 8263, 8269, 8273, 8287, 8291, 8293, 8297, 8311, 8317, 8329, 8353, 8363, 8369, 8377, 8387, 8389, 8419, 8423, 8429, 8431, 8443, 8447, 8461, 8467, 8501, 8513, 8521, 8527, 8537, 8539, 8543, 8563, 8573, 8581, 8597, 8599, 8609, 8623, 8627, 8629, 8641, 8647, 8663, 8669, 8677, 8681, 8689, 8693, 8699, 8707, 8713, 8719, 8731, 8737, 8741, 8747, 8753, 8761, 8779, 8783, 8803, 8807, 8819, 8821, 8831, 8837, 8839, 8849, 8861, 8863, 8867, 8887, 8893, 8923, 8929, 8933, 8941, 8951, 8963, 8969, 8971, 8999, 9001, 9007, 9011, 9013, 9029, 9041, 9043, 9049, 9059, 9067, 9091, 9103, 9109, 9127, 9133, 9137, 9151, 9157, 9161, 9173, 9181, 9187, 9199, 9203, 9209, 9221, 9227, 9239, 9241, 9257, 9277, 9281, 9283, 9293, 9311, 9319, 9323, 9337, 9341, 9343, 9349, 9371, 9377, 9391, 9397, 9403, 9413, 9419, 9421, 9431, 9433, 9437, 9439, 9461, 9463, 9467, 9473, 9479, 9491, 9497, 9511, 9521, 9533, 9539, 9547, 9551, 9587, 9601, 9613, 9619, 9623, 9629, 9631, 9643, 9649, 9661, 9677, 9679, 9689, 9697, 9719, 9721, 9733, 9739, 9743, 9749, 9767, 9769, 9781, 9787, 9791, 9803, 9811, 9817, 9829, 9833, 9839, 9851, 9857, 9859, 9871, 9883, 9887, 9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973]
for i in f:
    for x in range(44, 50):
        p= 2*(i**x)+ 1
        if n%p== 0:
            print(p)
            break

```
![image](https://hackmd.io/_uploads/rk5CPtvqa.png)

**Challenge 5: Mirror_World_1**
- Vời chall này ta thấy e= 3, ta sẽ nghĩ đến việc sử dụng CRT, tuy nhiên ta chỉ có một cặp giá trị (c, n). Mặt khác ta nhận ra rằng một lần nc đến sever, sever sẽ cung cấp cho ta một cặp giá trị (c, n) khác cùng encrypt 1 flag.
- Lợi dụng điểm này ta sẽ có được nhiều cặp giá trị (c, n) để khai thác.
- Sử dụng Hastad Attack ta thu được flag.

![image](https://hackmd.io/_uploads/Bkn5DKPcp.png)




### RSA
- Đây là source challenge:
```Python
from Crypto.Util.number import *
FLAG= b"Thisisfakeflag"

FLAG = bytes_to_long(FLAG)

if __name__ == "__main__":
    p = getPrime(512)
    q = getPrime(512)
    N = p*q
    e = 65537
    d = inverse(e, (p-1)*(q-1))
    c = pow(FLAG, e, N)
    print(f"N = {N}")
    print(f"c = {c}")
    while True:
        try:
            c = int(input(">>> "))
            bit = pow(c,d,N) % 2
            print(bit)
        except:
            break
```
- Ta nhận ra challenge sau có liên quan đến [Lsb attack](https://crypto.stackexchange.com/questions/11053/rsa-least-significant-bit-oracle-attack).
- LSB: 
    - Trước hết ta có 2 trường hợp sau:
        - TH1: n chẵn hay n= 2p. Này dễ decrypt rồi nên ta ko xét tiếp.
        - TH2: n lẻ hay n= pq
            - Xét RSA thuần không có trường hợp đặc biệt: 
                $$ Encrypt:\ c\equiv m^e\ (mod\ n)$$ $$Decrypt:\ m\equiv c^d\ (mod\ n)$$
            - Xét c:
                - Nếu c chẵn => m lẻ.
                    - Xét $2^ec\equiv (2m)^e\ (mod\ n) =>x \equiv 2m \equiv (2^ec)^d\ (mod\ n)$. 
                    - Mặt khác:
                    $$Nếu\ x (mod\ 2)= 0=> 2m> n <=> m> \frac{n}{2}$$ $$Nếu\ x(mod\ 2)= 1=> 2m< n<=> m< \frac{n}{2}$$
                - Nếu c lẻ=> m chẵn. (Xét tương tự trường hợp trên).
    - Mục đích của lsb attack là để ta thu nhỏ vùng giá trị của m từ đó có thể tìm được m một cách dễ dàng hơn.
- Ta sẽ giải mã với code sau:
```Python
from pwn  import*
from binascii import*
from Crypto.Util.number import*
import base64
def get_process():
    return remote("localhost", 1337)
def oracle(x):
    io.sendlineafter(b'> ', str(pow(x, e, n) * c % n).encode())
    return io.recvline()
io = get_process()
e = 65537
io.recvuntil(b'N = ')
n = int(io.recvuntil(b"\n").decode())
io.recvuntil(b'c = ')
c = int(io.recvuntil(b"\n").decode())
lb = 0
ub = n
k = 1
while True:
    k *= 2
    if oracle(k) == b"0\n":
        ub = ((ub + lb )//2) 
    else :
        lb = ((ub+lb)//2)  
    if (ub - lb) < 100:
        print(int(ub),int(lb))
        break
for i in range(ub+ 1, lb+ 1, -1):
    print(i.to_bytes((i.bit_length() + 7) // 8, 'big'))
```
![image](https://hackmd.io/_uploads/Hy-skmcFT.png)
