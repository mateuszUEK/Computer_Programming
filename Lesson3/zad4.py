age = float(input("Enter the dogs age: "))
result = 0

for i in range(1, int(age+1)):
    if i == 1 or i == 2:
        result += 10.5
    else:
        result += 4

print(f"Dogs age in dog years is: {result}")
