# This program requires Python 3

# Google Code Jam 2016 Qualification Round Problem A Counting Sheep
# https://code.google.com/codejam/contest/6254486/dashboard

# Problem: Bleatrix Trotter the sheep has devised a strategy that
# helps her fall asleep faster. First, she picks a number N. Then she
# starts naming N, 2 * N, 3 * N, and so on. Whenever she names a
# number, she thinks about all of the digits in that number. She keeps
# track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has
# seen at least once so far as part of any number she has named. Once
# she has seen each of the ten digits at least once, she will fall
# asleep.

# Bleatrix must start with N and must always name (i + 1) * N
# directly after i * N. For example, suppose that Bleatrix picks
# N = 1692. She would count as follows:

#    N = 1692. Now she has seen the digits 1, 2, 6, and 9.
#    2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
#    3N = 5076. Now she has seen all ten digits, and falls asleep.

# What is the last number that she will name before falling asleep? If
# she will count forever, print INSOMNIA instead.

# INPUT
# The first line of the input gives the number of test cases, T. T
# test cases follow. Each consists of one line with a single integer
# N, the number Bleatrix has chosen.

# OUTPUT
# For each test case, output one line containing Case #x: y, where x
# is the test case number (starting from 1) and y is the last number
# that Bleatrix will name before falling asleep, according to the
# rules described in the statement.  Limits

# 1 <= T <= 100.
# Small dataset

# 0 <= N <= 200.
# Large dataset

# 0 <= N <= 10^6


INFILE = "A-small-practice.in"
OUTFILE = "A-small-practice.out"


def stringToInt(loS):
    '''
    ListOfString -> ListOfInt

    >>> stringToInt(['4'])
    [4]
    >>> stringToInt([])
    []
    >>> stringToInt(['5', '75', '25'])
    [5, 75, 25]
    '''
    loi = []

    if loS == []:
        return []
    else:
        for i in range(len(loS)):
            loi.append(int(loS[i]))
        return loi


def load_file(infile):
    '''
    String -> ListOfInt
    Take a GCJ newline and space-delimited textfile and process it
    so that the entire file is a list with each line as a sublist
    made up of separate integers

    '5 10 15\n' -> [5, 10, 15]
    '''
    # List for storing entire infile
    inputL = []
    with open(infile, 'r') as f:
        for line in f:
            tempL = []
            line.replace('\n', '')
            # Split words on whitespace and insert in tempL
            tempL = line.split()
            # Convert tempL from LoS to LoI
            tempL = stringToInt(tempL)
            # Append LoI to inputL
            inputL.append(tempL)
    return inputL


def num_cases(list_file):
    '''
    ListOfInt -> Int

    Pop the first element from list_file (which should only contain ints)

    **NOTE**: this function mutates the input list!

    >>> num_cases([[5], [0], [1], [2], [11], [1692]])
    5
    '''
    ncases = list_file.pop(0)[0]
    return ncases


def next_case(list_file):
    '''
    ListOfInt -> Int
    Given a list of sublists of ints, return the next element
    which represents N, the number that Bleatrix Trotter starts
    counting from.

    **NOTE**: this function mutates the input list!

    >>> next_case([[0], [1], [2], [11], [1692]])
    0

    >>> next_case([])
    []
    '''
    if list_file == []:
        return []
    else:
        return list_file.pop(0)[0]


def digit_splitter(number):
    '''
    Int -> ListOfInt
    Split an integer into a list of its constituent digits

    >>> digit_splitter(1692)
    [1, 6, 9, 2]

    >>> digit_splitter(0)
    [0]

    >>> digit_splitter(11)
    [1, 1]
    '''

    num_digits = len(str(number))
    digitL = []

    for i in range(num_digits):
        digitL.append(number % 10)
        number = number // 10

    return digitL[-1::-1]


def count_digits(loi):
    '''
    ListOfInt -> DictOfInt
    Given a ListOfInt, for the keys 0 ~ 9, assign
    the count of each digit occurrence as dict key values

    >>> count_digits([1, 6, 9, 2])
    {0: 0, 1: 1, 2: 1, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 0, 9: 1}

    >>> count_digits([0])
    {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    '''

    zeroNineD = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0,
                 8:0, 9:0}

    for i in loi:
        zeroNineD[i] += loi.count(i)

    return zeroNineD


def zero_nine(zndict):
    '''
    Dict -> Boolean
    Given a dict containing the digits 0 ~ 9 as keys, return True
    if all the key values 0 ~ 9 are >= 1

    return False otw

    >>> zero_nine({0:1, 1:3, 2:1, 3:0, 4:0, 5:0, 6:1, 7:0, 8:0, 9:1})
    False

    >>> zero_nine({0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1})
    True

    >>> zero_nine({0:9, 1:8, 2:7, 3:6, 4:5, 5:4, 6:3, 7:2, 8:1, 9:1})
    True
    '''
    zn_flag = True
    # Index in list stands for each key in zndict, i.e. index 0
    # for key 0, index 1 for key 1, ...
    dgcountL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(zndict)):
        dgcountL[i] = zndict[i]

    for j in range(len(zndict)):
        if dgcountL[j] < 1:
            zn_flag = False

    return zn_flag


def update_dict(dold, dnew):
    '''
    Dict, Dict -> Dict
    Given two dicts containing the keys 0 ~ 9, create a new dict
    with the same keys but additive key values

    >>> update_dict({0:1, 1:0, 2:5}, {0:0, 1:1, 2:5})
    {0: 1, 1: 1, 2: 10}
    '''

    updateD = {}

    for i in range(len(dold)):
        updateD[i] = dold[i] + dnew[i]
    return updateD


def Bleatrix(sleepn):
    '''
    Int -> Int
    Int -> String

    1. Given an int 'sleepn' >= 0, return the final number when all digits
       0 ~ 9 have appeared.

    2. If all digits 0 ~ 9 can never appear, return the string "INSOMNIA"

    3. otw try sleepn * (i + 1)

    >>> Bleatrix(0)
    'INSOMNIA'

    >>> Bleatrix(1)
    10

    >>> Bleatrix(1000000)
    9000000
    '''
    bleatrixN = sleepn # the initial number N
    ncount = 1 # counter for sleepn

    if bleatrixN == 0:
        return "INSOMNIA"
    else:
        digList = digit_splitter(bleatrixN)
        digDict = count_digits(digList)

        if zero_nine(digDict):
            return bleatrixN
        else:
            while not zero_nine(digDict):
                ncount += 1
                bleatrixN = sleepn * ncount # N * (i+1)
                digDict_old = digDict
                digList_new = digit_splitter(bleatrixN)
                digDict_new = count_digits(digList_new)

                digDict = update_dict(digDict_old, digDict_new)
            return bleatrixN


def write_out(outfile):
    '''
    Write result to output file by calling helper functions
    load_file(), num_cases() and next_case() and logic function
    Bleatrix():
    1. load_file() strips newlines and adds strings to a list as ints,
       splitting on whitespace
    2. num_cases() gets the number of cases from the list created by
       load_file()
    3. next_case() returns the next case, N, a single integer >= 0
       to be analyzed by Bleatrix()
    4. Bleatrix() returns either the final N or the string Insomnia
    '''
    with open(outfile, 'w') as outf:
        input_list = load_file(INFILE)
        copy_input = input_list
        case_cnt = 1

        for i in range(num_cases(copy_input)):
            ans = Bleatrix(next_case(copy_input))
            outf.write('Case #' + str(case_cnt) + ': ' + str(ans) + '\n')
            case_cnt += 1


# MAIN PROGRAM
import doctest
doctest.testmod()
write_out(OUTFILE)
