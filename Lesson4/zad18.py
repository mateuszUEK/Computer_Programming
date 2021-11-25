def sumOfNumbers(n):
    sum = 0
    for digit in str(n): 
        sum += int(digit)      
    return sum
   
n = 7182
print(sumOfNumbers(n))
