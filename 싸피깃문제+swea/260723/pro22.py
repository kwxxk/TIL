a = [1,2,3]
N = int(input())

for i in range(N):
    move_fnum = a.pop(0)
    a.append(move_fnum)
print(a[0])