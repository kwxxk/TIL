char = int(input(    ))

if char % 4 == 0 and char % 100 != 0:
    print(1)
elif char % 400 == 0:
    print(1)
else:
    print(0)