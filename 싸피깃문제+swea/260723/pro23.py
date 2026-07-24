N = int(input())

get_input = list(map(int,input().split()))

get_input.sort()
print(*get_input, sep="")