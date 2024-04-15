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
