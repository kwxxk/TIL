arr = [ 'ABC', '77', '-33', '-33','125', 'ABC']
cnt = {}
for item in arr:
    if item in cnt:
        cnt[item] += 1
    else:
        cnt[item] = 1
target = input()

print(cnt[target])