arr = ['apple', 'banana', 'watermelon', 'strawberry']

# for element in arr:
#     print(element, end = ' ')

#초기화 (최대값이면 0)
length=0

for index, element in enumerate(arr):
    # 최대값 코드! 월말평가 나올 확률 100%
    if len(element) > length:
        length = len(element)
        len_max_index = index
    print(f"{index+1}번째 {element}", end = ' ')
print(f"{len_max_index+1}번째가 최대값")