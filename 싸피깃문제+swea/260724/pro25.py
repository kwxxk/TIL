arr = list(input().split())
cnt = {}
for char in arr:
    if char in cnt:
        cnt[char] += 1
    else:
        cnt[char] = 1

for key, value in cnt.items():
    print(key, value)