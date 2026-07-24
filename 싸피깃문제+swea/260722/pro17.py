arr = list(map(int, input().split()))

# flag = 0
# for i in arr:
#     if i % 2 == 0:
#         flag = 1
#         break

# print(flag)
def exist_even(numbers):
    for num in numbers:
        if num % 2 ==0:
            return 1
        
    return 0

flag = exist_even(arr)
print(flag)