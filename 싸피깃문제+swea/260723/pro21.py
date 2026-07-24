# # get_input = list(map(int,input().split()))
# get_input = []

# while True:
#     user_input = input()
#     if user_input == '0':
#         break
#     get_input.append(int(user_input))

# while get_input:
#     print(get_input.pop(), end="")

stack = []

while True:
    num = int(input())

    if num == 0:
        break

    stack.append(num)

word = ""
while len(stack) > 0: # 스택이 빌떄까지 반복
    word += str(stack.pop())

print(word)