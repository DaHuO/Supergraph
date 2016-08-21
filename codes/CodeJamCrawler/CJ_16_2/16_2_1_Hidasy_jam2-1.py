import sys

data = sys.stdin.read().split()
test_cases = data[0]
for index, test_case in enumerate(data[1:]):
    res = []
    test_case = list(test_case)

    ZEROS = [x for x in test_case if x == 'Z']
    num = len(ZEROS)
    for i in range(num):
        test_case.remove('Z')
        test_case.remove('E')
        test_case.remove('R')
        test_case.remove('O')
        res.append(0)

    EIGHT = [x for x in test_case if x == 'G']
    num = len(EIGHT)
    for i in range(num):
        test_case.remove('E')
        test_case.remove('I')
        test_case.remove('G')
        test_case.remove('H')
        test_case.remove('T')
        res.append(8)

    THREE = [x for x in test_case if x == 'H']
    num = len(THREE)
    for i in range(num):
        test_case.remove('T')
        test_case.remove('H')
        test_case.remove('R')
        test_case.remove('E')
        test_case.remove('E')
        res.append(3)

    TWO = [x for x in test_case if x == 'W']
    num = len(TWO)
    for i in range(num):
        test_case.remove('T')
        test_case.remove('W')
        test_case.remove('O')
        res.append(2)
    
    SIX = [x for x in test_case if x == 'X']
    num = len(SIX)
    for i in range(num):
        test_case.remove('S')
        test_case.remove('I')
        test_case.remove('X')
        res.append(6)

    SEVEN = [x for x in test_case if x == 'S']
    num = len(SEVEN)
    for i in range(num):
        test_case.remove('S')
        test_case.remove('E')
        test_case.remove('V')
        test_case.remove('E')
        test_case.remove('N')
        res.append(7)

    FOUR = [x for x in test_case if x == 'U']
    num = len(FOUR)
    for i in range(num):
        test_case.remove('F')
        test_case.remove('O')
        test_case.remove('U')
        test_case.remove('R')
        res.append(4)

    FIVE = [x for x in test_case if x == 'F']
    num = len(FIVE)
    for i in range(num):
        test_case.remove('F')
        test_case.remove('I')
        test_case.remove('V')
        test_case.remove('E')
        res.append(5)

    ONE = [x for x in test_case if x == 'O']
    num = len(ONE)
    for i in range(num):
        test_case.remove('O')
        test_case.remove('N')
        test_case.remove('E')
        res.append(1)

    NINE = [x for x in test_case if x == 'I']
    num = len(NINE)
    for i in range(num):
        test_case.remove('N')
        test_case.remove('I')
        test_case.remove('N')
        test_case.remove('E')
        res.append(9)

    res.sort()
    print("Case #{}: {}".format(index+1, ''.join([str(x) for x in res])))

# 0, 8, 3, 2, 6, 7, 4, 5, 1, 9
