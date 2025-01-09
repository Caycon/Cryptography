# from Crypto.Util.number import *

# flag= b'guess me if you can!'
# p = getPrime(512)
# q = getPrime(512)
# n = p*q
# e= 65537
# m= bytes_to_long(flag)
# c= pow(m,e,n)
# leaked_bits = p // (2**332) # or p >> 332
# print(f'{n= }')
# print(f'{e= }')
# print(f'{c= }')
# print(f'{leaked_bits= }')
# # flag= b'Fake flag is real!!!'


leaked_bits= 1317328585270738972473204167120977515658982227620979057
bin_leak= bin(leaked_bits)
print(f'{bin_leak= }')
p_real= str(bin(leaked_bits)) + 'x'*332
print(f'{p_real= }')