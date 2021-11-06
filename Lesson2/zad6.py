from random import randint
number = randint(1,6)

running = True
print("Guess the number: ")
while running:
    guess = int(input())
    if guess == number:
        print(f"Great job, {guess} is the correct answer")
        running = False
    else:
        print("Try again")
