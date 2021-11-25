file1 = open("zad18.txt", "r")

content = file1.read()
lines = content.split("\n")

file1.close()

file2 = open("zad18_copy.txt", "w")
for i in lines:
    file2.write(i)

file2.close()
