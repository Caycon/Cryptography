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
- Ngoài cách làm trên thì mình cũng có tham khảo 1 cách làm khác từ anh Quốc đó là dùng trực tiếp hàm `small_roots()` mà không cần dựng ma trận.
```python
from Crypto.Util.number import *

n= 89363852083183215084029975819623368020820853090098307473149845603341401045864934870570439256932632891265049547636998969703995375576460547095664091050686702009560848161533709748580943299702189297193534891972420842645361436489923822342004115286990841721297153500393107766316207595723258425173398506150683897157
e= 65537
c= 86806010536421428215138479024493529957254730212140712219406478401080347255310427820183046206405676261342754941707821722897347193983277842445151970816004013705244354576275846473959424227587946606819026532227502887761334668519249015633183869419896266715931667308536148698335454941446604091954057806509134160714
leaked_bits= 8519065679210462875347890550002311295807311144091750402590996981174033798178225468961955441999549942033

P.<x> = PolynomialRing(Zmod(n))
f = x + (leaked_bits << 170)
a= f.small_roots(X=2^172, beta = 0.2, epsilon=1/200)
leaked_bits = bin(leaked_bits)[2:]
leaked_bits= str(leaked_bits)+ "0"*(512-len(leaked_bits))
leaked_bits = int(leaked_bits,2)
p= int(leaked_bits+ a[0])
q= n/p
phi= (p-1)*(q-1)
d= pow(e, -1, phi)
m= pow(c, d, n)
print(long_to_bytes(m))
```

**Lý do chi tiết hơn thì tham khảo [ở đây](https://cr.yp.to/bib/1998/howgrave-graham.pdf)**

- Về phần **LSBs** thì ta sẽ xây dựng các đa thức cx như vector khác đi 1 chút

![image](https://github.com/user-attachments/assets/9d193ae1-53bf-4062-9b00-7fae4b777768)
- Ta sẽ xây dựng $f(x)$ có dạng $f(x)= 2^l*x+ leak$ với $l$ là số bits cần tìm.
- Ở đây mình sẽ **demo** lsb với `leak_d`.

##### Chall
```python
from Crypto.Util.number import *

p= getPrime(512)
q= getPrime(512)
n= p*q
e= 65537
flag= b'I_don_t_known_what_to_write_here'
m= bytes_to_long(flag)
phi= (p- 1)*(q- 1)
d= pow(e, -1, phi)
leak_d= int(bin(d)[500:], 2)
c= pow(m,e,n)
print(f'{n= }')
print(f'{e= }')
print(f'{c= }')
print(f'{leak_d= }')

# n= 92632196527519941289819350921056829444480517010265589957373778873700077999955727574845706207026646182464034351127633386337820727903030036940541823654138006668699194468568991659311510407657330799284138619308687017650347813053278313969556107745488764630509019514210739901312047621908667595656257612889224859869
# e= 65537
# c= 48046750041670335285068610235156253269884365678622418225768512605784894827053819086725640701415448606737196290908073774411377744841747389430504021560561291770507430714623168935334852338156759536737332034393066927373059032428769776355834331235798865293970127768809191936837184639844809659781883469696230478716
# leak_d= 68718016546295563418182894064324632202272387383594063947969268641966166712179179231739309696177871563473945009041717936543752257965771216357096765501676816449
```
##### Solution
```python
from Crypto.Util.number import *

n= 92632196527519941289819350921056829444480517010265589957373778873700077999955727574845706207026646182464034351127633386337820727903030036940541823654138006668699194468568991659311510407657330799284138619308687017650347813053278313969556107745488764630509019514210739901312047621908667595656257612889224859869
e= 65537
c= 48046750041670335285068610235156253269884365678622418225768512605784894827053819086725640701415448606737196290908073774411377744841747389430504021560561291770507430714623168935334852338156759536737332034393066927373059032428769776355834331235798865293970127768809191936837184639844809659781883469696230478716
leak_d= 68718016546295563418182894064324632202272387383594063947969268641966166712179179231739309696177871563473945009041717936543752257965771216357096765501676816449

D = len(bin(n)) - 2  # number of bits in n
R = D - 500  # so here R is roughly 724 (maybe)

# We also know that:
#    d = X * 2^R + leak_d,
# where X is the unknown 400-bit number.

# Our RSA equation is: e*d - k*phi(n) = 1.
# Note that for RSA, phi(n) = (p-1)(q-1) and k is a small positive integer.
# In fact, since d is “full‐size”, one typically has d ~ n so that k ≈ e.
#
# We now try candidates for k in a small interval around e.

delta = 65537
found = False
candidate_d = None

for k in range(e - delta, e + delta):
    if k <= 0:
        continue
    # The RSA relation gives: e*d ≡ 1 (mod k) so we expect d ≈ k*n/e.
    d_approx = (k * n) // e
    # Write d = X*2^R + leak_d, so an approximate X is:
    x_approx = (d_approx - leak_d) >> R  # equivalent to floor((d_approx - leak_d)/2^R)
    
    # Try a few offsets around x_approx
    for offset in range(-5, 6):
        X = x_approx + offset
        if X < 0:
            continue
        d_candidate = X * (1 << R) + leak_d
        # Check that the RSA relation holds: e*d_candidate - 1 must be divisible by k.
        if (e * d_candidate - 1) % k != 0:
            continue
        phi_candidate = (e * d_candidate - 1) // k
        
        # Recover p+q from phi(n) = n - (p+q) + 1  =>  p+q = n - phi_candidate + 1
        s = n - phi_candidate + 1
        # For correct p,q, the discriminant Δ = (p+q)^2 - 4n must be a perfect square.
        disc = s * s - 4 * n
        if disc < 0:
            continue
        sqrt_disc = math.isqrt(disc)
        if sqrt_disc * sqrt_disc != disc:
            continue
        p = (s + sqrt_disc) // 2
        q = (s - sqrt_disc) // 2
        if p * q == n:
            print(f'{p= }')
            print(f'{q= }')
            found = True
            break
    if found:
        break

if not found:
    print("[-] Failed to recover the key!")
    exit(1)

m = pow(c, d_candidate, n)
print(long_to_bytes(int(m)))
```

#### Leak bits in mid
![image](https://github.com/user-attachments/assets/61c2a3b9-dbb7-4419-aaab-8edfd2795ab4)
- Với dạng này thì sẽ khó hơn **MSBs hay LSBs**
- Cụ thể thì phần bits bị leak sẽ là $a$, lúc này:
$$p= x*2**t+ y+ a$$
- Với t là hiệu của số bits $p$ với số most bits chưa biết.

##### Chall
- Ở đây mình sẽ setup 1 chall với $leak_p$ bị ẩn 40 bits đầu và 47 bits cuối.
```python
from Crypto.Util.number import *
flag= b'I_am_chill_guy'
p= getPrime(512)
q= getPrime(512)
n= p*q
e= 65537
m= bytes_to_long(flag)
c= pow(m, e, n)
leak_p = int(bin(p)[2:].zfill(512)[40:465], 2) << 47
print(f'{n= }')
print(f'{e= }')
print(f'{c= }')
print(f'{leak_p= }')

# n= 95833140363150173085400781562336570561015616460313210023975270126616157131624528587272063057307225026161835408699888323499488279019129501329065630402087285258471135141986496693723213866761952112220188009361594959340470056360323997143701160632189890086147838319540477404939016199414749172031337591306156717957
# e= 65537
# c= 85585941751998800537891696785955548411294697759152457743742952506986880949373120940602110913029788782243069830692032701804087815911677859038561767938618923528464864146810669499058733566518068351509560838577248261272216817539613495749072417594986788748418531887477297026449652895516064864083462020309481181862
# leak_p= 446726636560982512156094109972620717668814180129313191107990193476358979707694308539854517523276106719891732860421584561376386167782984646656
```

##### Solution
- Ý tưởng của t sẽ là xây dựng một đa thức 2 ẩn $x; y$ để biểu diễn cho $p$ và từ đó tìm $p$ thông qua $x; y$.
- Ở đây ta có: $$f(x; y)= p= ax + y + leak_p$$
- Tiếp theo ta sẽ tạo đa thức dịch chuyển hay shifted polynomials.
- Mục tiêu chính là xây dựng một tập hợp các đa thức có cùng nghiệm nhỏ (x, y) mà ta cần tìm, từ đó “cắt xén” (eliminate) nhiễu và thu được đa thức có hệ số nhỏ dễ xử lý hơn. Nói cách khác, ta muốn tạo ra nhiều đa thức liên quan đến ẩn số (x, y) sao cho khi thay nghiệm chính xác vào, chúng có giá trị “nhỏ” (hoặc thậm chí bằng 0 modulo một số nào đó). Điều này là tiền đề để sau đó dùng các kỹ thuật lattice, qua bước giảm LLL, tìm ra được mối quan hệ “mịn” giữa các ẩn số.
- Xây dựng đa thức:
    - Đa thức ban đầu: $$f(x; y)= ax + y + leak_p$$
    với $p= ax + y + leak_p$. Do $n=pq$, nên nếu ta `scale` (nâng) hoặc `shifted` (dịch chuyển) $f(x; y)$ theo cách thích hợp, khi thay các giá trị (x, y) chính xác vào, các đa thức mới sẽ có một tính chất đặc biệt (thường là chia hết cho $𝑛$ hoặc có giá trị rất nhỏ).
    - Nhân với các đơn thức:
        - Trong kỹ thuật tìm nghiệm nhỏ của **Coppersmith** hay **Howgrave-Graham**, ta thường tạo ra các đa thức mới bằng cách nhân đa thức gốc với các đơn thức $x^iy^i$ (với deg của $xy$ không quá cao).
        - Với case này các cặp số mũ được lấy theo dạng: $$(h,i) \text{với} \ h+i <= deg \ \text{(deg= 4)}$$
    - Từ đây ta sẽ có 2 case khi tạo shifted polynomials:
        - Case 1: Khi $h= 0$:
            - Shifted polynomials: $$g(x; y)= nx^i.$$
            - Lý do có $n$ ở đây là để $g(x; y) \equiv 0\ mod(n)$ và không có $y$ dù là $g(x; y)$ là để biến đa thức thành 1 biến cho dễ giải quyết:))
        - Case 2: Khi $h> 0$:
            - Shifted polynomials: $$g(x; y)= f(x; y).x^iy^{h-1}$$
            - Ở đây ta nhân $f(x; y)$ với $x^iy^{h-1}$ để phân phối deg của $x; y$ trong đa thức. Khi đó đa thức mới có các bậc khác nhau của ( x ) và ( y ), từ đó xây dựng một hệ đa thức.
            - Cách xây dựng này giúp kéo dài không gian của các đa thức mà vẫn bảo toàn tính chất: khi thay nghiệm (x, y) chính xác vào, các đa thức này có giá trị nhỏ (hoặc $ \equiv 0 \ mod(n)$)
- Xây dựng **lattice**
    - Mỗi đa thức $g(x, y)$ có thể được biểu diễn dưới dạng tổng các đơn thức: $$g(x, y) = \sum_{(h, i)} c_{hi} x^h y^i$$
    - Ta tạo một ma trận **M**, trong đó mỗi hàng tương ứng với một đa thức dịch chuyển $g(x, y)$, và mỗi cột ứng với một đơn thức $x^h y^i$ (theo thứ tự của danh sách các cặp số mũ đã chọn).
    - Các đa thức ban đầu có thể có các hệ số với độ lớn rất khác nhau, làm cho lattice không cân bằng, do đó ta (scale) các hệ số của các đơn thức theo hai hằng số:
        - **scale_x**: Dùng cho các đơn thức chứa $x^h$. `scale_x` được chọn là $2^{(512-472)} = 2^{40}$.
        - **scale_y**: Dùng cho các đơn thức chứa $y^i$, với scale_y được chọn bằng $b = 2^{47}$.

```python
from Crypto.Util.number import *

n= 167580499956215950519401364953715382046426622073945444209826355141355616253284471005334650342162345240975585728731605368177279851073566181310579765061891014250502756284021540424912815047098023724780350364100609602779707167364816138138292881169029901637887077174119691465839709933394383980487654025215303169197
e= 65537
c= 139141713394182175338014160210574677242324318147310823544533218285438453679685360942557889405708630849117917919844618438631772469175157267044325855150684069102771610083706768718034754862646137870042713558761139906496513003195874156227906594994060711022603795992594839895900529076885908269590003750247551274645
leak_p= 11285951004747532118510977324365459146506394352712787708919871521893387325998280830757079994592547761237824232119473733009976060329355198332928

a = 2**(512 - 47)  
b  = 2**47      
deg = 4        

Pxy = PolynomialRing(Zmod(n), names=('x', 'y'))
x_mod, y_mod = Pxy.gens()

Pol_mod = a * x_mod + y_mod + leak_p

Pol_int = Pol_mod.change_ring(ZZ)
PR_int, (x, y) = Pol_int.parent().objgens()

exponent_pairs = [(k - i, i) for k in range(deg + 1) for i in range(k + 1)]
monomials = [PR_int(x**h * y**i) for (h, i) in exponent_pairs]

f_poly = Pol_int

g_list = []
for (h, i) in exponent_pairs:
    if h == 0:
        g_poly = n * (x**i)
    else:
        g_poly = f_poly * (x**i * y**(h - 1))
    g_list.append(g_poly)

scale_x = 2**(512 - 472)  
scale_y = b           
m_size = len(g_list)

M = Matrix(ZZ, m_size, m_size)
for row in range(m_size):
    for col in range(m_size):
        (h, i) = exponent_pairs[col]
        coeff = g_list[row][h, i]
        M[row, col] = coeff * (scale_x ** h) * (scale_y ** i)

B = M.LLL()

H = {}  
for i in range(B.nrows()):
    poly_H = PR_int(0)
    for j in range(B.ncols()):
        poly_H += PR_int((monomials[j] * B[i, j]) / monomials[j](scale_x, scale_y))
    H[i] = poly_H

PX = PolynomialRing(ZZ, 'xs')
xs = PX.gen()
PY = PolynomialRing(ZZ, 'ys')
ys = PY.gen()

res_x1 = H[0].resultant(H[1], y).subs(x=xs)
res_x2 = H[0].resultant(H[2], y).subs(x=xs)
poly_x = gcd(res_x1, res_x2)
x_root = poly_x.roots()[0][0]

res_y1 = H[0].resultant(H[1], x).subs(y=ys)
res_y2 = H[0].resultant(H[2], x).subs(y=ys)
poly_y = gcd(res_y1, res_y2)
y_root = poly_y.roots()[0][0]

p = a * x_root + y_root + leak_p
q = n // p
phi= (p-1)*(q-1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(long_to_bytes(int(m)))
```
