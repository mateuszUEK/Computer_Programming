x = int(input())
primes = []

for i in range(1, x+1):
    for j in range(2, x):
        if j != i and j != 1:
                continue
        else:
            primes.append(i)
print(primes)
