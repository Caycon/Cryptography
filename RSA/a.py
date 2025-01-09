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
