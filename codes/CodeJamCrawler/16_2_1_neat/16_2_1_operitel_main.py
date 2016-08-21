file = open('A-large.in', 'r')
output = open('A-large.ou', 'w')

def remove_array( arr1, arr2 ):
    for item in arr1:
        arr2.remove(item)
    return

T = int(file.readline().rstrip())
i = 1
for line in file:
    line = line.rstrip()
    array = [c for c in line]

    digits = []

    j = 0
    while j < len(array):
        if array[j] == 'Z':
            remove_array(['Z', 'E', 'R', 'O'], array)
            digits.append('0')
            j = -1 if (j - 4) < -1 else j - 4
        elif array[j] == 'W':
            remove_array(['T', 'W', 'O'], array)
            digits.append('2')
            j = -1 if (j - 3) < -1 else j - 3
        elif array[j] == 'U':
            remove_array(['F', 'O', 'U', 'R'], array)
            digits.append('4')
            j = -1 if (j - 4) < -1 else j - 4
        elif array[j] == 'X':
            remove_array(['S', 'I', 'X'], array)
            digits.append('6')
            j = -1 if (j - 3) < -1 else j - 3
        elif array[j] == 'G':
            remove_array(['E', 'I', 'G', 'H', 'T'], array)
            digits.append('8')
            j = -1 if (j - 5) < -1 else j - 5
        j += 1

    j = 0
    while j < len(array):
        if array[j] == 'S':
            remove_array(['S', 'E', 'V', 'E', 'N'], array)
            digits.append('7')
            j = -1 if (j - 5) < -1 else j - 5
        elif array[j] == 'O':
            remove_array(['O', 'N', 'E'], array)
            digits.append('1')
            j = -1 if (j - 3) < -1 else j - 3
        elif array[j] == 'H':
            remove_array(['T', 'H', 'R', 'E', 'E'], array)
            digits.append('3')
            j = -1 if (j - 5) < -1 else j - 5
        j += 1

    j = 0
    while j < len(array):
        if array[j] == 'F' or array[j] == 'V':
            remove_array(['F', 'I', 'V', 'E'], array)
            digits.append('5')
            j = -1 if (j - 4) < -1 else j - 4
        elif array[j] == 'N':
            remove_array(['N', 'I', 'N', 'E'], array)
            digits.append('9')
            j = -1 if (j - 4) < -1 else j - 4
        j += 1

    digits.sort()
    res = ''.join(digits)

    print('Case #' + str(i) + ': ' + str(res))
    output.write('Case #' + str(i) + ': ' + str(res) + '\n')
    i += 1

output.close()



