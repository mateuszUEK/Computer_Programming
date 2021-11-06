pin = "0805"

i = 0
while i < 3:
    answer = input("Enter the pin: ")
    if answer == pin:
        print("PIN number correct.")
        break
    else:
        print("incorrect")
    i+=1

if i == 3:
    print("Sorry, your payment card has been blocked.")
