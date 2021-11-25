file = open("colors.txt", "w")
tab = ["red", "green", "blue"]

for i in tab:
    file.write(f"{i}\n")

file.close()

