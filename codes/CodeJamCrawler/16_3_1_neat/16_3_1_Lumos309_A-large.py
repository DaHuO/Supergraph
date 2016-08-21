# GCJ 2016 Round 1C A-small

infile = open("A-large.in", "r")
outfile = open("A-large-output.txt", "w")

def quicksort(array):

    if array == []:
        return []

    else:
        less, greater = [], []
        midpoint = array[0]

        if array == []:
            return []

        for item in array[1:]:
            if item[1] < midpoint[1]:
                less.append(item)
            else:
                greater.append(item)

        return quicksort(greater) + [midpoint] + quicksort(less)


cases = infile.readline()
for case in range(int(cases[:-1])):
    string = infile.readline()
    string = infile.readline()
    string = string[:-1].split(' ')
    result = ''
    

    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    senators = [[alphabet, 0] for alphabet in alphabets]

    for i in range(len(string)):
        senators[i][1] = int(string[i])

    senators = quicksort(senators)

    print(senators)

    while senators[0][1] > senators[1][1]:
        if senators[0][1] - senators[1][1] >= 2:
            senators[0][1] -= 2
            result += senators[0][0] + senators[0][0] + ' '
        else:
            result += senators[0][0] + ' '
            senators[0][1] -= 1

    for i in range(2, len(senators)):
        while senators[i][1] > 1:
            senators[i][1] -= 2
            result += senators[i][0] + senators[i][0] + ' '
        if senators[i][1] == 1:
            result += senators[i][0] + ' '

    for i in range(senators[0][1]):
        result += senators[0][0] + senators[1][0] + ' '

    result += "\n"

    outfile.write("Case #{0}: {1}".format(str(int(case) + 1), result))


infile.close()
outfile.close()
    
