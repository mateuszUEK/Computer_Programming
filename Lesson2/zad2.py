height = 175
feet = int(height/30.48)
inches = int(round((height/30.48)%1, 1) * 10)
print(f"I am 175cm tall i.e. {feet} feet and {inches} inches tall")
