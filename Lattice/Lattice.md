# Introduct
- **Lattice** trong toán học là một tập hợp các điểm được xác định trong không gian nhiều chiều thông qua các tổ hợp tuyến tính của một tập hợp hữu hạn các vector cơ sở. Lưới thường được định nghĩa trong không gian `Euclid` n chiều, trong đó mỗi điểm trong lưới có tọa độ là các số nguyên. Vector cơ sở của lưới là các vector tạo thành một hệ thống độc lập tuyến tính, có thể tạo ra mọi điểm trong lưới thông qua các tổ hợp tuyến tính của chúng.
- Cụ thể, một lưới trong không gian n chiều có thể được biểu diễn như sau: $$L= ({v_1;v_2;v_3;....;v_n})$$
- Trong đó $({v_1;v_2;v_3;....;v_n})$ là các vector cơ sở của lưới, và mọi điểm trong lưới được biểu diễn như một tổ hợp tuyến tính của các vector cơ sở: $$v= a_1v_1+a_2v_2+....a_nv_n$$ $$(\text{Với}\ a_1;a_2;...;a_n\ \text{là các số nguyên}).$$
-  **Basis (Cơ sở)**: Một tập hợp các vector được gọi là một hệ cơ sở của lattice nếu mọi điểm trong lattice có thể được biểu diễn dưới dạng một tổ hợp tuyến tính của các vector trong hệ cơ sở đó.
- **Shortest Vector Problem (SVP, Vấn đề vector ngắn nhất)**: SVP là một trong những vấn đề quan trọng nhất trong lý thuyết lattice. Nó đặt ra câu hỏi: "Tìm vector cơ sở ngắn nhất của một lattice đã cho".
- **Closest Vector Problem (CVP, Vấn đề vector gần nhất)**: CVP là một vấn đề liên quan khác, trong đó bạn cần tìm vector trong lattice gần nhất với một điểm đã cho nào đó trong không gian.
- **Lattice Reduction (Giảm lattice)**: Đây là một kỹ thuật quan trọng để giảm độ phức tạp của lattice, giúp giải quyết các vấn đề như SVP và CVP hiệu quả hơn. Thuật toán giảm lattice nổi tiếng nhất là thuật toán LLL (Lenstra-Lenstra-Lovász).
- **Lattice-based Cryptography (Mật mã dựa trên lattice)**: Lý thuyết lattice cũng đóng vai trò quan trọng trong lĩnh vực mật mã. Các hệ thống mật mã dựa trên lattice thường không dễ bị tấn công bởi các thuật toán lượng tử và đang trở thành một lựa chọn phổ biến cho các ứng dụng mật mã hiện đại.
# Lattice
- Định nghĩa (Hệ mạng): Cho một cơ sở gồm $n$ vectơ có tọa độ thực với $n$ mục, hệ mạng được tạo bởi cơ sở đó là tập hợp các tổ hợp tuyến tính nguyên của các vectơ. Nói cách khác, $B = \{v_i = (x_{i1}, x_{i2}, \ldots, x_{in}): 0 < i < n, x_{ij} \in \mathbb{R} \ \forall i, j\}$, sau đó hệ mạng $L$ được đưa ra bởi $L = \mathcal{C}(B) = \{\sum_{i=1}^n a_i v_i: a_i \in \mathbb{Z}\}$. Ta cũng có thể viết $B$ để biểu thị một ma trận được hình thành bằng cách lấy các cột làm vectơ cơ sở:
$$\begin{align*}
B &= \begin{pmatrix}
b_{11} & b_{12} & \cdots & b_{1n} \\
b_{21} & b_{22} & \cdots & b_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
b_{n1} & b_{n2} & \cdots & b_{nn}
\end{pmatrix}&=
\begin{pmatrix}
\vec{v}_1 \\
\vec{v}_2 \\
\vdots \\
\vec{v}_n
\end{pmatrix}
\end{align*}
$$
**Ma trận unimodular:**
- Ma trận unimodular là ma trận có định thức bằng ±1.
- Nếu hai cơ sở B và C tạo ra cùng một mạng L, thì ma trận tương ứng của chúng được liên hệ bởi phép nhân với một ma trận unimodular U.
- Có thể biến đổi một cơ sở thành cơ sở khác bằng các phép toán cơ bản trên cột, bao gồm:
    - Đổi vị trí các cột.
    - Nhân một cột với -1.
    - Cộng một bội số của một cột với một cột khác.
# Vấn đề bài toán lattices
- Gồm có các bài toán như sau:
    - Bài toán vectơ gần nhất (CVP): Cho một vectơ v không thuộc mạng L, tìm vectơ u trong mạng L sao cho khoảng cách giữa v và u là nhỏ nhất. 
        > Closest Vector Problem (CVP): Cho một vector $(\vec{w} \in \mathbb{R}^n)$ không thuộc lattice $(\mathcal{L})$, tìm vector $(\vec{v}\in\mathcal{L})$ sao cho khoảng cách giữa chúng là ngắn nhất, $(\vert\vert\vec{v}-\vec{w}\vert\vert)$ là tối thiểu.
    - Bài toán vectơ ngắn nhất (SVP): Tìm vectơ u trong mạng L sao cho độ dài của u là khoảng cách ngắn nhất của mạng L.
        > Shortest Vector Problem (SVP):Cho lattice $(\mathcal{L})$, tìm $(\vec{v}\in\mathcal{L})$ sao cho $(\vert\vert\vec{v}\vert\vert=\lambda(\mathcal{L})).$
    - Bài toán vectơ ngắn nhất xấp xỉ (apprSVP): Tìm vectơ u trong mạng L sao cho độ dài của u nhỏ hơn hoặc bằng một giá trị xấp xỉ (phụ thuộc vào kích thước mạng) của khoảng cách ngắn nhất của mạng L.
        > Approximate Shortest vector problem (apprSVP): Giả sử $(\psi(n))$ là một hàm chỉ phụ thuộc vào $(n)$ và $(\mathcal{L})$ là một lattice có kích thước $(n)$. Bài toán vectơ ngắn nhất xấp xỉ $(\psi(n))$-apprSVP là tìm một vector $(\vec{v}\in\mathcal{L})$ sao cho độ dài của nó nhỏ hơn $(\psi(n))$ lần độ dài của vectơ ngắn nhất trong mạng. Hay nói cách khác $(\vert\vert\vec{v}\vert\vert\leq\psi(n)\lambda(\mathcal{L}))$, với $\lambda(\mathcal{L}))$ là độ dài của vectơ ngắn nhất trong mạng L.
# Một số thuật toán và định lý
**Định lý Hermite:**
- Với mọi lattice $(\mathcal{L})$, $\exists$ vector $\ne 0$ $(\vec{v}\in\mathcal{L})$ sao cho $(\vert\vert\vec{v}\vert\vert\leq \sqrt{n}\det(\mathcal{L})^{\frac 1 n})$.
**Hằng số Hermite:**
- Cho chiều n bất kỳ, Hằng số Hermite γ_n được định nghĩa là giá trị nhỏ nhất thỏa mãn tính chất: Mọi mạng Λ có chiều n đều chứa một vectơ khác vectơ không $v\in \mathbb{A}$ sao cho: $$(\vert\vert\vec{v}\vert\vert^2\leq \gamma_n \det(\mathcal{L})^{\frac 2 n})$$
- Trong đó, det(Λ) ký hiệu định thức của Λ. Do đó, theo định lý Hermite, thì $γ_n ≤ n$.
