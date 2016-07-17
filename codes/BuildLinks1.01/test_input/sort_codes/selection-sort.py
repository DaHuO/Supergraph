def selectionSort(u):
    for i in range(len(u) - 1):
        min = i
        for j in range(i+1,len(u)):
            if u[j] < u[min]:
                min = j
        if min != i:
            u[i], u[min] = u[min], u[i]
    return u
