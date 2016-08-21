t = int(input())
for i in range(1, t + 1):
    input_string = input()
    number = ""
    check1 = True
    temp = []
    for j in input_string:
        temp += [j]

    input_string = temp
    while check1 != False:
        first = input_string.count('Z')

        if first == 0:
            check1 = False
        else:
            number += '0'
            input_string.remove('Z')
            input_string.remove('E')
            input_string.remove('R')
            input_string.remove('O')

    check2 = True
    while check2 != False:
        first = input_string.count('W')
        if first == 0:
            check2 = False
        else:
            number +='2'
            input_string.remove('T')
            input_string.remove('W')
            input_string.remove('O')



    check3 = True
    while check3 == True:
        first = input_string.count('U')
        if first == 0:
            check3 = False
        else:
            number += '4'
            input_string.remove('F')
            input_string.remove('O')
            input_string.remove('U')
            input_string.remove('R')

    check4 = True
    while check4 == True:
        first = input_string.count('X')
        if first == 0:
            check4 = False
        else:
            number += '6'
            input_string.remove('S')
            input_string.remove('I')
            input_string.remove('X')

    check5 = True
    check6 = True
    check7 = True
    check8 = True
    check9 = True
    check0 = True
    while check5 == True:
        first = input_string.count('R')
        if first == 0:
            check5 = False
        else:
            number += '3'
            input_string.remove("T")
            input_string.remove("H")
            input_string.remove("R")
            input_string.remove("E")
            input_string.remove("E")

    while check6 == True:
        first = input_string.count('G')
        if first == 0:
            check6 = False
        else:
            number += '8'
            input_string.remove("E")
            input_string.remove("I")
            input_string.remove("G")
            input_string.remove("H")
            input_string.remove("T")

    while check7 == True:
        first = input_string.count('F')
        if first == 0:
            check7 = False
        else:
            number += '5'
            input_string.remove("F")
            input_string.remove("I")
            input_string.remove("V")
            input_string.remove("E")

    while check8 == True:
        first = input_string.count('V')
        if first == 0:
            check8 = False
        else:
            number += '7'
            input_string.remove("S")
            input_string.remove("E")
            input_string.remove("V")
            input_string.remove("E")
            input_string.remove("N")

    while check9 == True:
        first = input_string.count('I')
        if first == 0:
            check9 = False
        else:
            number += '9'
            input_string.remove("N")
            input_string.remove("I")
            input_string.remove("N")
            input_string.remove("E")

    while check0 == True:
        first = input_string.count('N')
        if first == 0:
            check0 = False
        else:
            number += '1'
            input_string.remove("O")
            input_string.remove("N")
            input_string.remove("E")

    

    output = ''.join(sorted(number))
    print("Case #{}: {}".format(i, output))


    # Z 0
    # W 2
    # U 4
    # X 6
    # R 3
    # G 8
    # F 5
    # V 7
    # I 9
    # N 1