# arr = [ 'ABC', '77', '-33', '-33','125', 'ABC']
# cnt = {}
# for item in arr:
#     if item in cnt:
#         cnt[item] += 1
#     else:
#         cnt[item] = 1
# target = input()

# print(cnt[target])

# 리스트 index, element
# 딕셔너리 key, value

arr = [ 'ABC', '77', '-33', '-33', '125', 'ABC']

d = dict()
for a in arr:
    # 딕셔너리의 key로
    d[str(a)] = 0 #0으로 초기화

for a in arr:
    d[str(a)] += 1 #카운팅

char = input()
print(d[char]) # value