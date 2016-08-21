def find_max(array):
    max1 = -1
    max2 = -1

    for i in range(len(array)):
        if array[i] > max1:
            max1 = array[i]
            idx1 = i

    array[idx1] -= 1

    for i in range(len(array)):
            if array[i] > max2:
                max2 = array[i]
                idx2 = i

    array[idx2] -= 1

    if (array[idx2] < 0):
        idx2 = -1

    return array, idx1, idx2

nb_test = int(input())

for t in range(1, nb_test + 1):
    n = int(input())
    parties = [int(x) for x in input().split()]
    y = []

    # total number of senators
    total = 0
    for i in range(n):
        total += parties[i]

    while total > 0:
        parties, idx1, idx2 = find_max(parties)
        if idx2 != -1:
            y.append(chr(65 + idx1) + chr(65 + idx2))
            total -= 2
        else:
            y.append(chr(65 + idx1))
            y_size = len(y)
            tmp = y[y_size - 1]
            y[y_size - 1] = y[y_size - 2]
            y[y_size - 2] = tmp
            total -= 1

    print("Case #" + str(t) + ": ", end="")
    print(" ".join(y))
