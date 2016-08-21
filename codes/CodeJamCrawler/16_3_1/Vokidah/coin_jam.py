def return_two_max(array):
    if array[0] >= array[1]:
        first_max = array[0]
        first_index = 0
        second_max = array[1]
        second_index =  1
    else:
        first_max = array[1]
        first_index = 1
        second_max = array[0]
        second_index = 0
    for i in range(2, len(array)):
        if array[i] >= first_max:
            second_index = first_index
            second_max = first_max
            first_max = array[i]
            first_index = i
        elif array[i] > second_max:
            second_max = array[i]
            second_index = i
    return first_max, second_max, first_index, second_index


T = int(input())
f = open('workfile', 'w')
for j in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    max1, max2, i1, i2 = return_two_max(array)
    result = ""
    while max1 != 1:
        if max1 != max2 and max2 / N < 0.5:
            result += "%s%s "%(chr(i1 + 65), chr(i1 + 65))
            array[i1] -= 2
        else:
            result += "%s%s " % (chr(i1 + 65), chr(i2 + 65))
            array[i1] -= 1
            array[i2] -= 1
        max1, max2, i1, i2 = return_two_max(array)
    count = 0
    for each in array:
        if each == 1:
            count += 1
    i = 0
    while count != 0 and i < len(array):
        if count % 2 == 0:
            step = 2
        else:
            step = 1
        while step != 0 and i < len(array):
            if array[i] == 1:
                step -= 1
                result += chr(i + 65)
                count -= 1
                array[i] -= 1
            i += 1
        result += ' '
    f.write("Case #%s: %s\n" % (j, result[:-1]))
    print(result)