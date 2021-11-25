file1 = open("zad17.txt", "r")

content = file1.read()

file1.close()

file2 = open("zad17_copy.txt", "w")

file2.write(content)

file2.close()
