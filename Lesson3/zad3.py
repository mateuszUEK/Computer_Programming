amount = float(input("Amount: "))

if amount / 5 >= 1:
    print(f"5 zl - {int(amount/5)}")
    amount = amount - (int(amount/5) * 5)
if amount / 2 >= 1:
    print(f"2 zl - {int(amount/2)}")
    amount = amount - (int(amount/2) * 2)
if amount / 1 >= 1:
    print(f"1 zl - {int(amount/1)}")
    amount = amount - (int(amount/1) * 1)


