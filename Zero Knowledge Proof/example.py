from py_ecc.optimized_bn128 import G1, G2, pairing, multiply

# Đọc các thử thách từ file output.txt
with open("output.txt", "r") as f:
    challenges = f.readlines()

flag_bits = []
for chal in challenges:
    xG, yG, zG = eval(chal.strip())  # Đọc và parse từng thử thách
    
    # Thực hiện phép pairing trên xG và yG
    pairing_result = pairing(yG, xG)
    
    # So sánh với zG để xác định bit
    if pairing_result == zG:
        flag_bits.append('1')
    else:
        flag_bits.append('0')

# Kết hợp các bit để tạo ra flag
flag_binary = ''.join(flag_bits)
flag = bytes.fromhex(hex(int(flag_binary, 2))[2:]).decode()

print(f"FLAG: {flag}")
