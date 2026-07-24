arr = list(map(int, input().split()))

lotto_num = set()
is_valid = True

for num in arr:
    if num < 1 or num > 45:
        is_valid = False
        break
    if num in lotto_num:
        is_valid = False
        break        
    lotto_num.add(num)

if is_valid:
    print("VALID")
else:
    print("INVALID")