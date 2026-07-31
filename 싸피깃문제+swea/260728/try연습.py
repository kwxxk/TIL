# EAFP (try-except 구조) : 권장 하지 않는 방법
# 예시 IndexError

# def get_v(arr, idx):
#     try:
#         return arr[idx]
#     except IndexError:
#         return -1


# arr = [1,2,3]
# result =  get_v(arr, 3)

# print(result)

#LBYL (if-else 구조)

def get_v(arr,idx):
    if 0 <= idx <= len(arr) -1: #인덱스 범위 안에 있을 경우만
        return arr[idx] # 인덱싱
    else:
        return -1

arr = [1,2,3]
result =  get_v(arr, 2)

print(result)