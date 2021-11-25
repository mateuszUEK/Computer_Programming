tab = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest = tab[0]
for i in tab:
    if len(i) > len(longest):
        longest = i
print(longest)
