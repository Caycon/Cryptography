**chall.py**
```python
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long
import binascii

# Tạo khóa RSA
key = RSA.generate(2048)
p = key.p
q = key.q
n = key.n
e = key.e
d = key.d

# Rò rỉ nhiều bit cao của p
leak_bits = 128  # Số bit cao bị rò rỉ
p_high_bits = p >> (p.bit_length() - leak_bits)

print("Public Key (n, e):")
print(f"n = {n}")
print(f"e = {e}")

print("\nRò rỉ nhiều bit cao của p:")
print(f"p_high_bits = {bin(p_high_bits)}")

# Mã hóa thông điệp
message = b'This is a secret message'
cipher = pow(bytes_to_long(message), e, n)

print("\nCiphertext:")
print(binascii.hexlify(long_to_bytes(cipher)).decode('utf-8'))
```

**Solved.py**
```python
from sage.all import *
from Crypto.Util.number import long_to_bytes, bytes_to_long, inverse
import binascii

# Thông tin công khai và rò rỉ
n = 19519203763269311920721431815437642949661227468095203371423489018035038664765847323283772811892331954401796367891097600768270958331756745193013402912246273015189230240767291588777517992467867742311097699972534495581833771483061185942058945486534997847159087685524534249531464923868034521342214171855494540329014753168793523724423449549988342771440911684543131948049884730656184842125275734565465020489038248179414057234065016941400202512314544518340698525920463664224204356864356294589112956200104358182759155693689082646855956039975931858785058111160229073962063797110634463783700306741103076132850492708757306454239
e = 65537
p_high_bits = 0b10111011110000000000000110000110010011100010011111010101010000110101000001010011110101100011010010101110010000110000000001100110
cipher_hex = '6e5f62919bd13d4ee151d83ef3c8d52a4c3615a9495d6e9d0cce559bd972f0532b2da13b6c0ff111039e79a36aa7576929924ebf23177824d65cf8bc8889b77903c80983cdf1fc13ff66fd820aa78621983dfcd9fdc612f4be5c00fb810f12d04afc3c4666fd624c2c57aab9a7f03ec41b16fb35705865bbd4fb228b1f56086d802fce96f85438b12df4a20426a51d77581597548e6c0db454a810f3091a1d40f3ab0cb68e2735b7efb2567188773f883f676936acab8a137124d29e83e5a7ca52def409eea0efa331205d84c71b28f32189c51088a018946d66e6f3a1bd510f6027ac27e388d5d5d0ac93ed41ecd3a4195dc52b688d0cd200652a1785a52644'
cipher = int(cipher_hex, 16)

PR.<x> = PolynomialRing(Zmod(n))
f = p_high_bits * 2^(2048 - 128) + x
x0 = f.small_roots(X=2^(2048 - 128), beta=0.5)[0]
p = p_high_bits * 2^(2048 - 128) + x0
q = n // p

# Tính d
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

# Giải mã thông điệp
message = pow(cipher, d, n)
print("\nDecrypted message:")
print(long_to_bytes(message))
```