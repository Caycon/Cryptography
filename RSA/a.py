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

R= 2^(512- 170)
M = matrix([[R^2, 2*R*a, a^2], [0, R, a], [0, 0, N]])
B = M.LLL()
P.<x> = PolynomialRing(Zmod(N))
f = B[0][0]*x^2/R^2+B[0][1]*x/R+B[0][2]
f = f.monic()
f.small_roots()