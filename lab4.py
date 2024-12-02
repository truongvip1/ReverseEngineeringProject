final_hash="26f2d45844bfdbc8e5a2ae67149aa6c50e897a2a48fbf479d1bfb9f0d4e24544"
print(len(final_hash))
import hashlib
from itertools import product

# Tập hợp các ký tự để brute force
# flag_comp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
flag_comp = '0123456789'

# Giá trị hash cần brute force
target_hash = '26f2d45844bfdbc8e5a2ae67149aa6c50e897a2a48fbf479d1bfb9f0d4e24544'  # Thay giá trị bằng hash thực tế

def brute_force_sha256(flag_comp, target_hash, max_length=6):  # Thử từ độ dài 1 đến max_length
    for attempt in product(flag_comp, repeat=max_length):
        attempt_str = ''.join(attempt)
        # print(attempt_str)
        hashed_value = hashlib.sha256(attempt_str.encode()).hexdigest()
        # print(hashed_value)
        if hashed_value == target_hash:
            return attempt_str
    return None

# Chạy brute force
cp ="""
C8DBBF4458D4F226
C5A69A1467AEA2E5
79F4FB482A7A890E
4445E2D4F0B9BFD1
"""
result=[]
cp = cp.split('\n')
for i in cp:
    a = bytearray.fromhex(i)
    a = a[::-1]
    for j in a:
        result.append(j)

result = brute_force_sha256(flag_comp, target_hash, max_length=6)
if result:
    print(f"Chuỗi tìm được: {result}")
else:
    print("Không tìm thấy chuỗi phù hợp.")