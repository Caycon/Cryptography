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
- Nghe có vẻ giống phần trên tuy nhiên phần này thì ta sẽ làm việc với $p, q$ thay vì trực tiếp với $m$ như ở trên.
#### Kịch bản
- Với case này thì chall sẽ leak cho ta 1 phần của $p$, $q$ hoặc $p+ q$,... rất nhiều trường tuy nhiên đại khái là sẽ leak cho ta **1 phần bits liên tiếp** của 1 thứ gì đó liên quan đến **private key**.

![image](https://github.com/user-attachments/assets/15969f4a-31e4-4523-a936-d5c9b036a720)

- Ở đây thì mình sẽ triển khai và demo thử với trường hợp bị leak 1 phần bits liên tiếp của $p$.
- Cụ thể thì với case này ta sẽ cần ít nhất là $p^{\frac{1}{3}}$ bits liên tiếp bị leak để có thể giải được một cách nhanh chóng, việc biết ít hơn $p^{\frac{1}{3}}$ bits có thể khiến ta không giải được hoặc mất thời gian lâu hơn để có thể giải.
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
leaked_bits = p // (2**332) # or p >> 332
print(f'{n= }')
print(f'{e= }')
print(f'{c= }')
print(f'{leaked_bits= }')
# flag= b'Fake flag is real!!!'
```

`output.txt`
```text
n= 93263616157944058919846875466463090347899581927286723198825712303056123994104256872626205207965279457895808523638110948705977482041823584624522750931053653438999108145768784132338850701480328832257300425323448707035377867599405544355444911534470929526537809426991371877343290758765806901686459560093815787103
e= 65537
c= 90481003794365648689758133455679717012432939144766066412662619511781676510905016286093368716282389140821108056041040647090374833396303316827728871216587049143080339464044326686964337441664883102549647376405803297151229619882338062911783408571704214501758247375464168441204498042577637077318631684166194040034
leaked_bits= 1317328585270738972473204167120977515658982227620979057
```

#### Solution
- Từ code ta có thể biết được private key cụ thể là $p$ đã bị leak 180 bits đầu.
```python
leaked_bits= 1317328585270738972473204167120977515658982227620979057
bin_leak= bin(leaked_bits)
print(f'{bin_leak= }')
p_real= str(bin(leaked_bits)) + 'x'*332
print(f'{p_real= }')

# bin_leak= '0b110111000000111010001100101101110001101000100101111001001110000110001010000010100010101110000000110100111100010110110100110001001000110100010110110001100101011100001110000101110001'
# p_real= '0b110111000000111010001100101101110001101000100101111001001110000110001010000010100010101110000000110100111100010110110100110001001000110100010110110001100101011100001110000101110001xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```
- Trực qua thì ta có như trên, giờ vấn đề là làm các nào để ta có thể tìm lại $p$ để giải.
- Từ đây ta có được: $p= leak+ x$ với $x$ là phần chưa biết cần tìm. Mặt khác ta có $pq=n$.
- Hay $r*q \equiv -leak*q \mod n$