from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from os import urandom
from pwn import xor, process, remote
from base64 import b64encode, b64decode
from tqdm import tqdm
#io = process(['python3', 'aes-cbc.py'])
io = remote("34.162.82.42", 5000)

plaintext = b"I am an authenticated admin, please give me the flag"
p1 = b'I am an authenti'
p2 = b'cated admin, ple'
p3 = b'ase give me the '
p4 = pad(b'flag', 16)

io.recvuntil(b'Your choice: ')
io.sendline(b'1')
res = b64decode(io.recvline().strip().decode())
iv = b'\0x00'*16

def padding_oracle(p, block):   
    pad =  16 * bytes([0])
    I = [0]*16
    c1 = b''
    for i in range(1, 17):
        for j in tqdm(range(1,256)):
            io.recvuntil(b'Your choice: ')
            io.sendline(b'2')
            payload = pad[:16-i] + bytes([j]) + c1
            msg = iv + payload + block
            io.sendline(b64encode(msg).decode())
            oracle_reply = io.recvline()
            if b'Unknown command!' in oracle_reply:
                I[16 - i] = j ^ i
                c1 = xor(bytes([i+ 1])*i , bytes(I[16 - i:]))
                break
    return xor(p, I)

c4 = urandom(16)
c3 = padding_oracle(p4, c4)
c2 = padding_oracle(p3, c3)
c1 = padding_oracle(p2, c2)
forged_iv = padding_oracle(p1, c1)
forged_ct = c1+c2+c3+c4

print(forged_iv, forged_ct)

io.recvuntil(b'Your choice: ')
io.sendline(b'2')
io.sendline(b64encode(forged_iv+forged_ct).decode())
io.interactive()