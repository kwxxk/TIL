# a = [1,2,3]
# N = int(input())

# for i in range(N):
#     move_fnum = a.pop(0)
#     a.append(move_fnum)
# print(a[0])

n = int(input())

friends = []
friends.append(1)
friends.append(2)
friends.append(3)

#N번 자리 바꾸기
for i in range(n):
    # 맨 앞에 친구를 빼서 (선출)
    front = friends.pop(0)
    # 맨 뒤에 추가 (선입)
    friends.append(front)

# 맨 앞의 친구를 출력(답)
print(friends[0]) #인덱싱