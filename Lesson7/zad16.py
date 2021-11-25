file = open("zad16.txt", "r")

content = file.read()
lines = content.split("\n")

count = 0
for i in lines:
    count += 1
    if count % 5 == 0:
        input("press enter")
    else:
        print(i)

file.close()
