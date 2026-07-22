arr = list(map(int, input().split()))

value= float('-inf') #음의 무한대
for index, element in enumerate(arr):
    if element > value:
        value = element
        max_index = index
print(f"리스트의 최대값은 {max_index+1}번쨰 {value}입니다")
