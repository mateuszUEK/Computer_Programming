number = int(input("Input a number: "))
result = number

for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
