rangeStart = int(input("Range start: "))
rangeEnd = int(input("Range end: "))
number = int(input("Number: "))

def isInRange(n):
    if n >= rangeStart and n <= rangeEnd:
        return True
    return False
print(isInRange(number))
