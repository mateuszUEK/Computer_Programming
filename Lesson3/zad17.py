i = 1
x = 1
for i in range(1, 8):
    if x != 1:
        x += i
    print(i, end=" ")
    for j in range(1, 7):
        print(x + 7, end=" ")
        x += 7
    print()
    x=0
