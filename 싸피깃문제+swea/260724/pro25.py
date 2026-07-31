# arr = list(input().split())
# cnt = {}
# for char in arr:
#     if char in cnt:
#         cnt[char] += 1
#     else:
#         cnt[char] = 1

# for key, value in cnt.items():
#     print(key, value)

arr = input().split() # 바로 리스트로 들어감
d = dict()
for a in arr:
    d[str(a)] = 0 # key값의 value 0으로 초기화

for a in arr:
    d[str(a)] += 1 #counting

for i in d: #딕셔너리는 키를 기준으로 순회
    print(i,d[i])