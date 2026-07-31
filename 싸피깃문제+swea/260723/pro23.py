# N = int(input())

# get_input = list(map(int,input().split()))

# get_input.sort()
# print(*get_input, sep="")

n = int(input())
numbers = list(map(int, input().split()))

#숫자들 오름차순 정렬
numbers.sort()

#정렬된 숫자 이어 붙이기
result = ""
for num in numbers: #iterator 방식 순회
    result += str(num) #문자열로 바꾼후 이어붙이기

print(result)