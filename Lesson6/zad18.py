i = 0
tab = []

def bubbleSort(array):
    n = len(array)
 
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]

while i < 3:
    for j in range(5):
        j = int(input())
        tab.append(j)

    bubbleSort(tab)
    print(tab)
    i += 1
    tab.clear()
