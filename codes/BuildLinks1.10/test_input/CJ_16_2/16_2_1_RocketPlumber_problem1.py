__author__ = 'shant_000'

# non decreasing order
# Identify uniques in each number
#if it contains a z, it contains zero etc



def remove_digit(digit, numstring):
    global nums_contained
    # if digit == 0:
    #     while 'z' in numstring:
    #         numstring.remove('z')
    #         numstring.remove('e')
    #         numstring.remove('r')
    #         numstring.remove('o')
    #         nums_contained += '0'
    #         print("currently at " + nums_contained)
    # if digit == 1:
    #     while 'o' in numstring and 'n' in numstring and 'e' in numstring:
    #         numstring.remove('o')
    #         numstring.remove('n')
    #         numstring.remove('e')
    #         nums_contained += '1'
    # if digit == 2:
    #     while 'w' in numstring:
    #         numstring.remove('t')
    #         numstring.remove('w')
    #         numstring.remove('o')
    #         nums_contained += '2'
    # if digit == 3:
    #     while 'h' in numstring and 'g' not in numstring:
    #         numstring.remove('t')
    #         numstring.remove('h')
    #         numstring.remove('r')
    #         numstring.remove('e')
    #         numstring.remove('e')
    #         nums_contained += '3'
    # if digit == 4:
    #     while 'u' in numstring:
    #         numstring.remove('f')
    #         numstring.remove('o')
    #         numstring.remove('u')
    #         numstring.remove('r')
    #         nums_contained += '4'
    # if digit == 5:
    #     while 'f' in numstring and 'i' in numstring and 'v' in numstring and 'e' in numstring:
    #         numstring.remove('f')
    #         numstring.remove('i')
    #         numstring.remove('v')
    #         numstring.remove('e')
    #         nums_contained += '5'
    # if digit == 6:
    #     while 'x' in numstring:
    #         numstring.remove('s')
    #         numstring.remove('i')
    #         numstring.remove('x')
    #         nums_contained += '6'
    # if digit == 7:
    #     while 'v' in numstring:
    #         numstring.remove('s')
    #         numstring.remove('e')
    #         numstring.remove('e')
    #         numstring.remove('v')
    #         numstring.remove('n')
    #         nums_contained += '7'
    # if digit == 8:
    #     while 'g' in numstring:
    #         numstring.remove('e')
    #         numstring.remove('i')
    #         numstring.remove('g')
    #         numstring.remove('h')
    #         numstring.remove('t')
    #         nums_contained += '8'
    # if digit == 9:
    #     while 'n' in numstring and 'i' in numstring and 'e' in numstring:
    #         numstring.remove('n')
    #         numstring.remove('i')
    #         numstring.remove('n')
    #         numstring.remove('e')
    #         nums_contained += '9'


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    nums_contained = ""
    numstring = input()
    numstring = numstring.lower()
    numstring = list(numstring)
    while 'z' in numstring:
        numstring.remove('z')
        numstring.remove('e')
        numstring.remove('r')
        numstring.remove('o')
        nums_contained += '0'
    while 'g' in numstring:
        numstring.remove('e')
        numstring.remove('i')
        numstring.remove('g')
        numstring.remove('h')
        numstring.remove('t')
        nums_contained += '8'
    while 'h' in numstring and 'g' not in numstring:
        numstring.remove('t')
        numstring.remove('h')
        numstring.remove('r')
        numstring.remove('e')
        numstring.remove('e')
        nums_contained += '3'
    while 'w' in numstring and 't' in numstring and 'o' in numstring:
        numstring.remove('t')
        numstring.remove('w')
        numstring.remove('o')
        nums_contained += '2'
    while 'u' in numstring and 'f' in numstring and 'o' in numstring and 'r' in numstring:
        numstring.remove('f')
        numstring.remove('o')
        numstring.remove('u')
        numstring.remove('r')
        nums_contained += '4'
    while 'f' in numstring and 'i' in numstring and 'v' in numstring and 'e' in numstring:
        numstring.remove('f')
        numstring.remove('i')
        numstring.remove('v')
        numstring.remove('e')
        nums_contained += '5'
    while 'x' in numstring and 's' in numstring and 'i' in numstring:
        numstring.remove('s')
        numstring.remove('i')
        numstring.remove('x')
        nums_contained += '6'
    while 'v' in numstring and 's' in numstring and 'n' in numstring and 'e' in numstring:
        numstring.remove('s')
        numstring.remove('e')
        numstring.remove('e')
        numstring.remove('v')
        numstring.remove('n')
        nums_contained += '7'

    while 'n' in numstring and 'i' in numstring and 'e' in numstring:
        numstring.remove('n')
        numstring.remove('i')
        numstring.remove('n')
        numstring.remove('e')
        nums_contained += '9'
    while 'o' in numstring and 'n' in numstring and 'e' in numstring:
        numstring.remove('o')
        numstring.remove('n')
        numstring.remove('e')
        nums_contained += '1'
    x = list(nums_contained)
    x.sort()
    nums_contained = ''.join(x)
    print("Case #" + str(i) + ": " + nums_contained)

