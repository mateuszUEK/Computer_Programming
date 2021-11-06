quantity = 0
mySum = 0
while 1:
    number = int(input("Enter number: "))
    if number == 0:
        break
    else:
        quantity += 1
        mySum += number
        mean = mySum/quantity
print(f"Quantity = {quantity}, Sum = {mySum}, Mean = {mean}")
