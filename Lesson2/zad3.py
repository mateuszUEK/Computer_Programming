import math
a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))
s = (a + b + c)/2
print(math.sqrt(s*(s-a)*(s-b)*(s-c)))
