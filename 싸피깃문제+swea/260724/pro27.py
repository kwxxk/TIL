# arr = list(map(int, input().split()))

# lotto_num = set()
# is_valid = True

# for num in arr:
#     if num < 1 or num > 45:
#         is_valid = False
#         break
#     if num in lotto_num:
#         is_valid = False
#         break        
#     lotto_num.add(num)

# if is_valid:
#     print("VALID")
# else:
#     print("INVALID")
numbers = list(map(int, input().split()))

# 우선순위 1순위
if len(numbers) != 6:
    print("INVALID")
else: #길이가 6인 경우
    lotto_set = set()
    for num in numbers:
        if 1<= num <= 45:
            lotto_set.add(num)
    if len(lotto_set) == 6: # 로또의 숫자 개수가 6개
        print('VALID')
    else:# 로또의 숫자 갯수가 6개도 안될때
        print("INVALID")

