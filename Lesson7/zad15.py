file = input("File name: ")
lineCount = 0

fileName = open(file, "r")

content = fileName.read()
lines = content.split("\n")
  
for i in lines:
    if i:
        lineCount += 1
          
print(f"Number of lines: {lineCount}")
