# Elliptic Curve Cryptography
## Đường cong Ellipptic
- Đường cong `Ellipptic` E trên trường K là đường cong được xác định bằng phương trình sau:
$$E:\ y^2+ a_1xy+ a_3y= x^3+ a_2x^2+ a_4x+ a_5$$
- Trong đó $a_1,\ a_2,\ a_3,\ a_4,\ a_6 \in K$ và $\Delta \ne 0$:
$$\begin{cases}
\Delta= -d_2d_8-8d^{3}_4- 27d^{2}_6+ 9d_2d_4d_6\\
d_2= a^{2}_1+ 4a_2\\ 
d_4= 2a_4+ a_1a_3\\ 
d_6= a^{2}_3+ 4a_6\\
d_8= a^{2}_1a_6+ 4a_2a_6- a_1a_3a_4+ a_2a^{2}_2-a^{2}_4\end{cases}$$
- Mặt khác ta có thể biến đổi phương trình đường cong `Ellipptic` thành phương trình sau khi đặc số trường K khác 2:
$$(y+ \frac{a_1x}{2}+ \frac{a_3}{2})^2= x^3+ (a_2+  \frac{a^{2}_1}{4})x^2+ (a_4+ \frac{a_1a_3}{2})x+ (\frac{a^{2}_4}{3}+ a_6)$$ $$=>y^{2}_1= x^3+ a'_2x^2+a'_4x+ a'_6$$
- Với đặc số K> 3:
$$E: y_1^2= x^3_1+ Ax+ B$$
    - Khi đó $\Delta= -16(4A^3+ 27^2)$.
- Nếu L là trường mở rộng bất kỳ của K thì tập hợp các điểm hữu tỷ L trên E là:
$$E(L) = {(x, y) ∈ L × L : y^2 +a_1xy +a_3y − x^3 −a_2x^2 −a_4x −a_6 = 0} ∪ {∞}\ \text{là điểm ở vô cùng}$$
![image](https://hackmd.io/_uploads/rkgNNxNT6.png)
## Các phép toán trên đường cong Ellipptic.
###  Phép cộng trên Ellipptic.

- Xét hai điểm $P_1= (x_1; y_1);\ P_2(x_2;\ y_2) \in E:\ y^2+ a_1xy+ a_3y= x^3+ a2x^2+ a_4x+ a_6$. Phép cộng giữa 2 điểm trên đường cong E được định nghĩa như sau:
$$P_3(x_3;\ y_3)= P_1= (x_1; y_1)+ P_2(x_2;\ y_2)$$
- Trong đó $P_3(x_3;\ y_3)= -P'_3(x_3;\ y'_3)$ là giao điểm của đường cong E và đường thẳng đi qua $P_1;\ P_2$. Vì $P_3(x_3;\ y_3)\ và\ -P'_3(x_3;\ y'_3)$ đều nằm trên E nên $(x_3;\ y_3)\ và\ (x_3;\ y'_3)$ đều phải thỏa mãn phương trình E. Từ đó ta có hình minh họa sau:
![image](https://hackmd.io/_uploads/rJ7wLcSTp.png)
- Xét đường thằng đi qua $P_1;\ P_2$ có phương trình:
$$y= \alpha x+ \beta \ \(1.0)$$
#### Với $P_1 \ne P_2$.
- Từ (1.0) ta có:
$$y_1- y_2= \alpha (x_1- x_2)$$ $$<=> \alpha= \frac{y_1- y_2}{x_1- x_2}\ \(*)$$
- Mặt $\ne$: (1.0) $=> \beta= y_1- \alpha x_1\ \(**)$
- Từ (*)(**):
$$=> \beta= y_1- \frac{y_1- y_2}{x_1- x_2}x_1= \frac{x_1y_1- x_2y_1}{x_1- x_2}$$
- Vậy: 
$$y= \frac{y_1- y_2}{x_1- x_2}x+ \frac{x_1y_1- x_2y_1}{x_1- x_2}$$
- Với $P_1; P_2$ là 2 điểm đối xứng trên đường cong `E`, khi đó $P_3= P_1+ P_2$ sẽ là điểm vô cùng và thuộc đường cong `E`.
#### Với $P_1 \equiv P_2$
- Ta có $\alpha= \frac{3x^2_1+ a_4}{2y_1}$
- Đường thẳng đi qua $P_1; P_2$ tiếp tuyến với `E` cắt `E` tại Q thì Q chính là điểm cần tìm khi tính tổng của $P_1; P_2$.
- Các tính chất của phép cộng trên E:
     - $P + O = O + P = P\ \ (\forall P \in E).$
     - $P + (−P) = O\ \ (\forall P \in E).$
     - $(P + Q) + R = P + (Q + R)\ \ (\forall P,Q,R \in E).$
     - $P + Q = Q + P\ \ (\forall P,Q \in E).$
     - $P, Q$ đối xứng nhau qua trục hoành hay $Q = -P$.  Nghịch đảo của $P$ : $-P = -(x,y) = (x, -y).$
### Phép nhân trên Ellipptic
 **Nhân vô hướng:**
 - Với $n \in \mathbb{N^*}$ và $P$ là điểm thuộc đường cong Ellipptic, ta có $nP$ sẽ là phép cộng của $n$ lần $P$:
$$\begin{equation}
P-> P_n = \underbrace{P + P + \dots + P}_{n \text{ lần}} = Q
\end{equation}$$
- Để tối ưu phép nhân vô hướng, có thể sử dụng phương pháp Nhân đôi-và-cộng, đầu tiên biểu diễn số n dưới dạng: $n = n_0 + 2n_1 + 2^2n_2+.....+ 2^mn_m\ với [n_0...n_m] \in {0, 1}$, sau đó áp dụng thuật toán:
```
Q ← 0
for i = 0 to m do
 if ni = 1 then
     Q ← CộngĐiểm(Q,P)
 end if
 P ← NhânĐôi(P)
end for
return Q
```
- Ngòai phương pháp Nhân đôi-và-cộng, có thể sử dụng phương pháp Trượt-cửasổ. Các phương pháp này cho phép nhân vô hướng một cách tối ưu.
- Lưu ý:
    - Không tồn tại phép nhân 2 điểm trên đường cong E, có nghĩa là không tồn tại $P.Q\ với\ P; Q \in E$.
    - Không tồn tại thuật toán chia vô hướng $Q: n$. Biết rằng $Q = nP$, bài toán tìm số n là bài toán Logarithm rời rạc. Đây là bài toán khó, thông thường phải thử lần lượt $n = 1, 2, . . . , n− 1$ phép cộng điểm $P$, cho đến khi tổng bằng $Q$, tuy nhiên có một số thuật toán tối ưu hơn để tìm n nhưng vẫn không thể giải được bài toán này trong thời gian đa thức vì thế dựa vào độ khó này có thể xây dựng ra hệ mật đường cong Elliptic với các giao thức cho mã hóa, xác thực và trao đổi khóa.
 ![image](https://hackmd.io/_uploads/H1LrO-IT6.png)
## Logarithm rời rạc
- Định nghĩa: Bài toán Logarithm rời rạc trên đường cong Elliptic $(ECDLP)$:
    - Cho đường cong E trên trường hữu hạn $\mathbb{F_q}$, điểm $P \in E(\mathbb{F_q})$ với bậc $n (nP = O = ∞)$ và điểm $Q \in E(\mathbb{F_q})$, tìm số nguyên $k \in [0, n − 1]$ sao cho $Q = kP$. Số nguyên k được gọi là Logarithm rời rạc của Q với cơ sở P, và thường được viết là $k = log_PQ$.
    - Việc tìm lại số $k$ là bài toán Logarit rời rạc - một bài toán khó có thể giải được trong thời gian đa thức.
    - Thuật toán tốt nhất hiện nay để tấn công bài toán ECDLP là sự kết hợp của thuật toán Pohlih-Hellman và Pollard's rho, thuật toán này có độ phức tạp thời gian tính toán là $O(\sqrt{p})$ với $p$ là ước số nguyên tố lớn nhất của  n do đó phải chọn số n sao cho nó chia hết cho số nguyên tố $p$ lớn nhất có $\sqrt{p}$ đủ lớn để giải bài toán này.
    
**Có một số phương pháp giải quyết Logarithm rời rạc như: [Baby-step giant-step](https://en.wikipedia.org/wiki/Baby-step_giant-step), [Pohlig-Hellman](https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm), [MOV attack](https://crypto.stanford.edu/pbc/notes/elliptic/movattack.html).**
### Baby-step giant-step
- Cho nhóm chu kỳ G cấp n, a là một phần tử sinh $\alpha$ của nhóm và một phần tử nhóm $\beta$. Giờ ta cần tìm $x$ sao cho:
$$\alpha ^{x}= \beta$$
- Ta sẽ tính:
$$m= \sqrt{n}$$
$$a^j\ với\ j=0, 1, ...., m- 1$$ $$\text{Lặp lại i từ}\ 0-> m-1:\text{Check xem}\ a^{im+ j}= \beta$$ $$\text{Nếu đúng thì:}\ x= im+ j\ \text{là giá trị cần tìm}.$$
- Baby step:
    - Ta chia khoảng tìm kiếm nghiệm $x$ thành $m$ phần, mỗi phần có $m$ giá trị.
    - Việc tính toán trước α^j giúp ta có thể nhanh chóng kiểm tra xem $α^{im + j}$ có bằng $\beta$ hay không.
- Giant step:
    - Ta "nhảy" qua $m$ giá trị mỗi lần, giúp giảm số lượng phép toán cần thực hiện.
    
**Thuật toán có độ phức tạp thời gian là $O(\sqrt{n})$.**
**Ví dụ:**

- Giả sử $n = 16, m = 4$.
- Baby step: 
    - Ta chia khoảng tìm kiếm nghiệm $x$ thành 4 phần: $[0, 3], [4, 7], [8, 11], [12, 15]$.
    - Trong mỗi phần, ta tính toán trước $α^j$ cho $j = 0, 1, 2, 3$.
- Giant step:
    - Bắt đầu từ $i = 0$, ta kiểm tra xem $α^{im + j}$ có bằng β hay không, với $j = 0, 1, 2, 3$.
Nếu không, ta chuyển sang $i = 1$ và lặp lại quá trình kiểm tra.
    - Tiếp tục cho đến khi tìm được nghiệm $x$.
**Thuật toán:**
>Chọn $m ≥\sqrt{N}$ và tính $mP$.
Tính và lưu trữ danh sách $iP$ với $0 ≤ i < m.$
Tính $Q − jmP$ với $j = 0, 1, . . . , m − 1.$
if $iP = Q − jmP$ then
$\ \ \ \ \ \ \ k = i + jm( mod N)$
end if
Quay về bước 3
    
### Pohlig-Hellman
 - Cho P, Q là các phần tử trong nhóm hữu hạn G bậc N. Ta muốn tìm một số nguyên k với $kP = Q$. Giả sử biết phân tích ra thừa số nguyên tố của $N$ là: $N= \prod_{i}n_i^{e_i}$
 - Phương pháp Pohlig - Hellman thực hiện tốt nhất nếu tất cả các ước nguyên tố của N là nhỏ. Nếu ước nguyên tố lớn nhất xấp xỉ lớn của N thì phương pháp khó áp dụng. Vì lý do này các hệ mật dựa trên logarit rời rạc thường chọn bậc của nhóm có chứa một thừa số nguyên tố lớn
 - Pohlig-Hellman - rút gọn các phép tính logarit rời rạc về các nhóm con nguyên tố cấp P và sử dụng Định lý số dư Trung Hoa để giải hệ đồng dư cho logarit rời rạc cấp toàn phần
 - Thuật toán Pohlig-Hellman hoạt động như sau:
     - Giả sử $n = q_1^{e1}*q_2^{e2}*...*q_i^{ei}$
     - Tính $l_i = l \ mod \ q_i^{ei}$ (1&lt;= i &lt;= r)
     - Sử dụng định lý thặng dư trung hoa để tính $$ l ≡ l_1 \ (mod \ q_1^{e1})$$ $$ l ≡ l_2 \ (mod \ q_2^{e2})$$ $$ ... $$ $$ l ≡ l_i \ (mod \ q_i^{ei})$$ 
     - Ở đây $q_1, q_2,..., q_i$ là tập hợp nguyên tố cùng nhau gồm các số nguyên dương, $gcd(q_i, q_j) = 1$. $l_1, l_2, ..., l_i$ đều là các số nguyên dương sao cho $0 \leq l_i <q_i$. Số nguyên dương duy nhất l có thể được tính toán một cách hiệu quả bằng cách sử dụng Thuật toán Euclide mở rộng.
     - $l_i=z_0+z_1q^1+z_2q^2+...+z_{e-1}q^{e-1}$ , $z_i \in [0, p-1]$
     - $P_0= \frac{n}{q_i}$ và $Q_0= \frac{n}{q_i}Q$
     - Khi đó $Q_0 = lP_0 = z_0P_0$
     - ta có thể tìm $z_0$ bằng $\frac{N}{q}Q =\frac{N}{q}(z_0 + z_1q + z_2q^2 +· · ·) P = \frac{N}{q}z_oP + (z_1+z_2q)NP = z_0 \frac{N}{p}P$ (NP = ∞)
     - Tương tự như vậy ta có thể tìm $z_1, z_2, z_3 ...$
### Tấn công MOV
 - Tấn công MOV liên quan đến việc tìm các điểm độc lập tuyến tính và tính toán ghép cặp Weil để giảm ECDLP xuống trường hữu hạn thay vì nhóm điểm trên đường cong elip
 - Mã giả thuật toán
1. Chọn một điểm ngẫu nhiên $T \in E(F_pm)$
2. Tính bậc $M$ của $T$
3. Đặt $d = gcd(M, N)$, $T_1 = (M / d)T$. Khi đó $T_1$ có bậc $d$ chia hết cho $N$, vậy $T_1 \in E[N]$
4. Tính $S_1 = e_N(P, T_1)$ và $S_2 = e_N(P, T_2)$. Khi đó cả $S_1, S_2$ đều thuộc vào $U_d \in F_p^*m$
5. Giải bài toán logarit rời rạc $S_2 = S_1^k$ trong $F_p^*m$. Kết quả cho ta $k(mod \ N)$
6. Lặp lại với các điểm ngẫu nhiên $T$ đến khi Lcm của các số $d$ khác nhau thu được là $N$. Khi đó ta xác định được $k(mod\ N)$.
