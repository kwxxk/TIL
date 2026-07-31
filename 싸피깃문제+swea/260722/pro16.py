a=[0,0,0,0,0]

for i in range(len(a)):
    
    # func = list(map(lambda x: x+5, a))
    a[i] += 5
    # b=range(5)

    # result = [x + y for x,y in zip(a,b)]
    for j in range(i):
        a[i] += 1
# print(*result)
print(*a)