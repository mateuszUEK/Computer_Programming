a = int(input("Input the value of a: "))
b = int(input("Input the value of b: "))

for i in range(0, a+1):
    for j in range (0, b+1):
        if i == 0 or i == a:
            print("*", end = "")
        elif j == 0 or j == b:
            print("*", end = "")
        else: 
            print(" ", end = "")
    print()
