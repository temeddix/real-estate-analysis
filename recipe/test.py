import re

sample = 'A2": "1111010100", "A3": "서울특별시 종로구 청운동", "A4": "1",'
filtered = re.sub(r"[^\x00-\x7F]+", "", sample)
print(filtered)
