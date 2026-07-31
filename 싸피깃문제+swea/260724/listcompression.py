# 0으로 초기화한 리스트를 만들어라
# pythonic한 방법 # 1번

# visited 배열 초기화 (나중에 개념설명)
visited = [0] * 10

# 1번
# for _ in range(5) -> 의미 5번 반복하는 코드 
data1 = [[0] * (5) for _ in range(5)]  # 5행 5열

# 1번 같은 코드
ret_arr = []
arr = [0] * 5
for _ in range(5):
    ret_arr.append(arr)

print(ret_arr)


# 2번
data2 = [[0 for _ in range(5)] for _ in range(5)] # 5행 5열

