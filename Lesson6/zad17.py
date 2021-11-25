tab1 = [4,36,12,28,9,44,5]
tab2 = [5,1,36]

appears = False
for i in tab1:
    for j in tab2:
        if i == j:
            appears = True
    if appears == False:
        print (i)
    appears = False
