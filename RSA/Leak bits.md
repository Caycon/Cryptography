# Introduct
- Ở đây mình sẽ trình bày 1 số trường hợp leak bits trong RSA thường gặp.
- Leak bits ở đây mình đề cập tới là một số trường hợp bits của private key bị leak 1 phần đủ để ta có thể sử dụng các kỹ thuật để ta có thể khôi phục lại từ đó decrypt được ciphertext.
- Tuy nhiên tùy vào trường hợp và độ dài của bits bị leak cũng như độ dài khóa được sử dụng mà thời gian recover key có thể mất khá nhiều thời gian.
## Demo
### Padding
#### Kịch bản

![image](https://github.com/user-attachments/assets/851d6c96-57b1-45ba-b217-73b1c1996669)

- Với case này **plaintext** đã được pad 1 số bytes vào. Tuy nhiên lại cho ta biết các bytes đó nằm ở vị trí như thế nào hoặc không (lúc này ta có thể brute force).
- Cụ thể thì case này cho ta giá trị của $c$, $n$, $e \ (small)$, $a$ (chuỗi được pad vào **plantext**), vị trí **plaintext** khi pad hoặc không:))).

**Demo:**

`chall.py`
```python
from Crypto.Util.number import *

a= b'I think len flag is 10- 16 bytes and '
flag= b'guess me if you can!'
p= getPrime(512)
q= getPrime(512)
n= p*q
e= 3
m= bytes_to_long(a+ flag)
c= pow(m, e, n)
print(f'n= {n}')
print(f'c= {c}')
# flag= b'crypto is cry'
```

`output.txt`
```text
n= 154650126490910825870431824934576182333068222671724410440155023178036767655133979421221274290173069244049735304064481949737997738636139682820002608333682194079520003991577040792761175190838968676570220075436336115063486472047547672850240504644724237622681051226475298641021460465693591328198884643113299290547
c= 42283915594501344485267248623513200233446094470736705697443007113321626680426285450382367899651284974513612737494846341451839719107790834231527235849133044523610427579413634210403497384575053059028736898829336544509930253507823130816774793407886244665524126325815927718654844171168338168469830396958711749844
```
#### Solution 
- Ta xác định được 
```python
m= b'I think len flag is 10- 16 bytes and '+ flag
```
- Với gợi ý là len flag khoảng 10- 16 bytes.
- Từ đây ta viết m:
```python
m= b'I think len flag is 10- 16 bytes and '
for i in range (10, 17):
    x= m+ b'\x00'* i
    print(x)

# b'I think len flag is 10- 16 bytes and \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
# b'I think len flag is 10- 16 bytes and \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
# b'I think len flag is 10- 16 bytes and \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
# b'I think len flag is 10- 16 bytes and \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
# b'I think len flag is 10- 16 bytes and \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
# b'I think len flag is 10- 16 bytes and \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
# b'I think len flag is 10- 16 bytes and \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
```

- Từ đây ta có thể lập được $f(x)= (a+ x)^3- c$ và $f(m) \equiv 0 \mod(n)$ do chưa biết chính xác len của flag nên ta sẽ brute force với tất cả giá trị $m$ ở trên.
- Ta sẽ sử dụng `small_roots()` do nghiệm cần tìm khá nhỏ ($max(2^{16})$).
- `small_roots(X, beta)` cho phép ta tìm nghiệm nhỏ của đa thức dựa trên LLL:
    - `X`: Giới hạn trên cho các nghiệm nhỏ cần tìm.
    - `beta`: Một tham số điều chỉnh độ chính xác của thuật toán (thường là 1).
- Ở đây điều khó nhất đó là dựng được $f(x)$, tuy nhiên với case này thì $f(x)$ khá dễ dựng.
```python
from Crypto.Util.number import *
n= 154650126490910825870431824934576182333068222671724410440155023178036767655133979421221274290173069244049735304064481949737997738636139682820002608333682194079520003991577040792761175190838968676570220075436336115063486472047547672850240504644724237622681051226475298641021460465693591328198884643113299290547
c= 42283915594501344485267248623513200233446094470736705697443007113321626680426285450382367899651284974513612737494846341451839719107790834231527235849133044523610427579413634210403497384575053059028736898829336544509930253507823130816774793407886244665524126325815927718654844171168338168469830396958711749844
e= 3
a= b'I think len flag is 10- 16 bytes and '
for i in range (10, 17):
    m= a+ b'\x00'* i
    m= bytes_to_long(m)
    P.<x> = PolynomialRing(Zmod(n))
    f= (m+ x)^e- c
    flag= f.small_roots()
    try:
        print(long_to_bytes(int(flag[0])))
    except: continue
```
- Ở đây ta xây dựng $f(x)= (m+ x)^e- c$ được luôn là do sau $flag$ không có bytes nào. Nếu sau $flag$ có bytes thì $f(x)$ sẽ được xây dựng khác.
- Giả dụ như $m$ có dạng sau:
```python
flag= b'if you know,'
m= b'Do you know '+ flag+ b' you know???'
```
- Lúc này thì $f(x)= (m+ 256^{12}x)^3- c$ do sau $x$ còn 12 bytes nữa nên ta phải nhân $x$ để đảm bảo $x$ nằm đúng vị trị của nó.
- Trực quan hơn ta có hiểu như sau:
```python
from Crypto.Util.number import *
flag= b'if you know,'
m_real= b'Do you know '+ flag+ b' you know???'
m_fake= b'Do you know '+ b'\x00'* len(flag)+ b' you know???'
print(f'{m_real= }')
print(f'{m_fake= }')
print(bytes_to_long(m_real))
print(bytes_to_long(m_fake))
flag1= bytes_to_long(m_real)- bytes_to_long(m_fake)
print(f'{flag1= }')
print(long_to_bytes(flag1))

# m_real= b'Do you know if you know, you know???'
# m_fake= b'Do you know \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 you know???'
# 132944776391389577397949188269005157229929023385782646936174071553984230557773543194431
# 132944776391389577397949188266420782912101888943572799252485287504916497230177197047615
# flag1= 2584374317827134442209847683688784049067733327596346146816
# b'if you know,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
```
- Dạng chall này có thể biến đổi bằng cách sử dụng random để tùy biến ẩn đi số bytes padding hoặc vị trí của flag. Từ đó ta phải brute force hoặc làm gì đó (ai biết ddoouu:)))

### Leak consecutive bits
- Nghe có vẻ giống phần trên tuy nhiên phần này thì mình sẽ chỉ thực hiện với $p, q$ thay vì trực tiếp với $m$ như ở trên.
#### MSBs- LSBs
- Mình chỉ demo nhỏ về **MSBs** còn về **LSBs** thì cũng sẽ khá tương tự.
##### Kịch bản
- Với case này thì chall sẽ leak cho ta 1 phần của $p$, $q$ hoặc $p+ q$,... rất nhiều trường tuy nhiên đại khái là sẽ leak cho ta **1 phần bits liên tiếp** của 1 thứ gì đó liên quan đến **private key**.

![image](https://github.com/user-attachments/assets/15969f4a-31e4-4523-a936-d5c9b036a720)

- Ở đây thì mình sẽ triển khai và demo thử với trường hợp bị leak 1 phần bits liên tiếp của $p$.
- Cụ thể thì với case này ta sẽ cần ít nhất là $p^{\frac{2}{3}}$ bits liên tiếp bị leak (đối với lattice 3x3) để có thể giải được một cách nhanh chóng, việc biết ít hơn $p^{\frac{2}{3}}$ bits có thể khiến ta không giải được hoặc mất thời gian lâu hơn để có thể giải.
- Demo dưới đây sẽ là về **MSBs** của p

**Demo**

`chall.py`
```python
from Crypto.Util.number import *

flag= b'guess me if you can!'
p = getPrime(512)
q = getPrime(512)
n = p*q
e= 65537
m= bytes_to_long(flag)
c= pow(m,e,n)
leaked_bits = p // (2**170) #or p >> 180
print(f'{n= }')
print(f'{e= }')
print(f'{c= }')
print(f'{leaked_bits= }')
# flag= b'Fake flag is real!!!'
```

`output.txt`
```text
n= 89363852083183215084029975819623368020820853090098307473149845603341401045864934870570439256932632891265049547636998969703995375576460547095664091050686702009560848161533709748580943299702189297193534891972420842645361436489923822342004115286990841721297153500393107766316207595723258425173398506150683897157
e= 65537
c= 86806010536421428215138479024493529957254730212140712219406478401080347255310427820183046206405676261342754941707821722897347193983277842445151970816004013705244354576275846473959424227587946606819026532227502887761334668519249015633183869419896266715931667308536148698335454941446604091954057806509134160714
leaked_bits= 8519065679210462875347890550002311295807311144091750402590996981174033798178225468961955441999549942033
```

##### Solution
- Từ code ta có thể biết được private key cụ thể là $p$ đã bị leak 342 bits đầu.
```python
leaked_bits= 8519065679210462875347890550002311295807311144091750402590996981174033798178225468961955441999549942033
bin_leak= bin(leaked_bits)
print(f'{bin_leak= }')
p_real= str(bin(leaked_bits)) + 'x'*170
print(f'{p_real= }')

bin_leak= '0b111100110110110111111011010101110111111001011011000001001101111000111100111101101010000110100100001011100001111010100110011010010010000100111110100111011110101000110001111100100111001101010010010001001101110100100011111010011000100000001011011101000101110010111111000111010000110001110001101011111110001010001101100110100011011100100100010001'
p_real= '0b111100110110110111111011010101110111111001011011000001001101111000111100111101101010000110100100001011100001111010100110011010010010000100111110100111011110101000110001111100100111001101010010010001001101110100100011111010011000100000001011011101000101110010111111000111010000110001110001101011111110001010001101100110100011011100100100010001xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```
- Trực quan thì ta có như trên, giờ vấn đề là làm các nào để ta có thể tìm lại $p$ để giải.
- Từ đây ta có thể thấy được nếu ta thay `x` thành `0` và `1` thì ta có thể giới hạn được giá trị của $p$ tuy nhiên khoảng cách vẫn là khá lớn nếu ta brute force từng số lẻ một. Do đó ở đây mình dựng ma trận M (r là giá trị cần tìm $p= leak+ r$):
```python
[ r**2; leak*r;    0]
[    0;      r; leak]
[    0;      0;    N]
```
- Hiện h ta cần tìm r hay x ($x= r$) để $g(r) \equiv \mod p$. Với: $$f(x)= x(x+leak)$$ $$g(x)= x+ a$$
- Ta chọn 3 vector lần lượt là:

$$v_0= (r^2;r*leak;0)$$
$$v_1= (0; r; leak)$$ 
$$v_2= (0; 0; n)$$
- Với ma trận trên thì ta có thể dùng với RSA- 1024, RSA- 2048 tuy nhiên lượng bits bị leak phải lớn hơn $p^{\frac{2}{3}}$.

```python
from Crypto.Util.number import *

n= 89363852083183215084029975819623368020820853090098307473149845603341401045864934870570439256932632891265049547636998969703995375576460547095664091050686702009560848161533709748580943299702189297193534891972420842645361436489923822342004115286990841721297153500393107766316207595723258425173398506150683897157
e= 65537
c= 86806010536421428215138479024493529957254730212140712219406478401080347255310427820183046206405676261342754941707821722897347193983277842445151970816004013705244354576275846473959424227587946606819026532227502887761334668519249015633183869419896266715931667308536148698335454941446604091954057806509134160714
leaked_bits= 8519065679210462875347890550002311295807311144091750402590996981174033798178225468961955441999549942033

leaked_bits = bin(leaked_bits)[2:]
leaked_bits= str(leaked_bits)+ "0"*(512-len(leaked_bits))
leaked_bits = int(leaked_bits,2)
r= 2**170
M= matrix([[r**2, r*leaked_bits, 0], [0, r, leaked_bits], [0, 0, n]])
A= M.LLL()
P.<x> = PolynomialRing(Zmod(n))
f = A[0][0]*x**2/r**2+A[0][1]*x/r+A[0][2]
f = f.monic()
a= f.small_roots()
p= int(leaked_bits+ a[0])
q= n/p
phi= (p-1)*(q-1)
d= pow(e, -1, phi)
m= pow(c, d, n)
print(long_to_bytes(m))
```
- Tùy vào việc chọn vector mà bài toán có thể được giải quyết nhanh hay chậm. Tuy nhiên việc chọn được vector sẽ cần khá nhiều kỹ năng và việc ước lượng để có chọn được vector sao cho có thể tìm được nghiệm là một vấn đề rất quan trọng.
- Lý do tại sao ở đây mình đề cập đến việc phải leak ít nhất $p^{\frac{2}{3}}$ là để đảm bảo ma trận 3x3 hoạt động được.
- Thực tế nếu chỉ có khoảng $p^{\frac{1}{3}}$ bits bị leak thì ta cũng có recover private key được, tuy nhiên lúc đó ta phải mở rộng đa thức cũng như ma trận, đồng thời xây dựng các vector phức tạp hơn.

**Lý do chi tiết hơn thì tham khảo [ở đây](https://cr.yp.to/bib/1998/howgrave-graham.pdf)**

- Về phần **LSBs** thì ta sẽ xây dựng các đa thức cx như vector khác đi 1 chút

![image](https://github.com/user-attachments/assets/9d193ae1-53bf-4062-9b00-7fae4b777768)
- Ta sẽ xây dựng $f(x)$ có dạng $f(x)= 2^l*x+ leak$ với $l$ là số bits cần tìm.

#### Leak bits in mid
![image](https://github.com/user-attachments/assets/61c2a3b9-dbb7-4419-aaab-8edfd2795ab4)
- Với dạng này thì sẽ khó hơn **MSBs hay LSBs**