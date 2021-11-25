file1 = open("MeatAndFish.txt", "r")
file2 = open("GrainsAndBread.txt", "r")

content1 = file1.read()
content2 = file2.read()

file3 = open("shoppingList.txt", "w")

file3.write(content1)
file3.write(content2)

file1.close()
file2.close()
file3.close()
