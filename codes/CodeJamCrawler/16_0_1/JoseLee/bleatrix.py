from math import *
import sys

def karatsuba(x,y):
    B = 10

    # recursion base case
    if x < B or y < B:
        return x*y

    # m set to be length of x or y, whichever is maximum
    # m = max(len(str(x)), len(str(y)))
    m = max(int(log10(x) + 1), int(log10(y) + 1))

    # check whether m is even. If odd, set m lower by 1
    if m % 2 != 0:
        m -= 1
    m_2 = int(m/2)

    a, b = divmod(x, B**m_2)
    c, d = divmod(y, B**m_2)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a+b), (c+d)) - ac - bd

    return ((ac*(B**m)) + bd + ((ad_bc)*(B**m_2)))


def find_and_check(num, onetozero):
    #print "find_and_check({0},{1})".format(num, onetozero)
    if len(onetozero) == 0:
        return None
    
    numstr = str(num)
    len_onetozero = len(onetozero)

    for i in range(len_onetozero-1, -1, -1):
        ind = numstr.find(onetozero[i])
        if ind > -1:
            del(onetozero[i])
    
    return onetozero


def solveit(N):
    if N == 0:
        return "INSOMNIA"

    onetozero = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    is_stop = False
    multip = 1
    while is_stop == False:
        kN = karatsuba(multip, N)
        onetozero = find_and_check(kN, onetozero)
        if (onetozero is None) or (len(onetozero) == 0):
            is_stop = True
            return kN 
        multip += 1


if __name__ == '__main__':
    # open input file
    # read first line of the file and put it to max_test
    # read whole file and put numbers into array
    # close the file
    # start loop i = 1 to i <= max_test
    #   pass first number to solveit()
    #   write output "Case #{0}: {1}".format(i, solveit(N))
    #   i += 1
    script, inpf = sys.argv
    maxtest = 0

    with open(inpf, 'r') as inp:
        lines = inp.readlines()
    lines = [int(line.rstrip('\n')) for line in lines]
    maxtest = lines[0]
    tests = lines[1:]

    for testn in range(0, maxtest):
        result = solveit(tests[testn])
        print "Case #{0}: {1}".format(testn+1, result)

