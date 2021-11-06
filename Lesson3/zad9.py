x = 5
for i in range(1, 5):
    for j in range(0, i):
        print(f"* ", end = "")
    print()
for k in range(5, 0, -1):
    for l in range(0, x):
        print(f"* ", end = "")
    x-=1
    print()
