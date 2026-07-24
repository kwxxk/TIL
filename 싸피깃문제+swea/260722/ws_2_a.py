zero_list = [0]
print(zero_list)

rows = 1
cols = 250000
many_zero_list=[0 for _ in range(cols) for _ in range(rows)] 
print(len(many_zero_list))

numbers = range(1,11)
print(list(numbers))

print(list(numbers[3:11]))