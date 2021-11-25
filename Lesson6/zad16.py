tab = [2, 6, 4, 9, 3]

def star(n):
    print(f"{n}: ", end ="")
    for i in range(n):
        print("*", end = " ")

for i in tab:
    star(i)
    print("")
