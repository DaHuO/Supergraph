import sys
import math
import string
import itertools

def formatOutput(n, result):
    return 'Case #' +  str(n) + ': ' + result + '\n'


def getDiv(n):
    i = 2
    is_prime = True
    limit = min(math.sqrt(n), 1000)
    while is_prime and i <= limit:
        is_prime = ((n % i) != 0)
        i += 1
    return (0 if is_prime else i - 1)


def getDivs(seq):
    base = 2
    has_prime = False
    divs = []
    while not has_prime and base <= 10:
        div = getDiv(int(seq, base))
        has_prime = div == 0
        divs.append(div)
        base += 1
    return divs, has_prime


def solveProblem(line):
    n, j = (int(x) for x in line.split())
    #strings = ['1' + val + '1' for val in [str(bin(x)[2:].zfill(n-2)) for x in range(0, pow(2, n-2))]]
    #values  = { val: [int(val, base) for base in range(2,11)] for val in strings }
    #dividers = { val: [getDiv(x) for x in values[val]] for val in strings }
    #results = [ val for val in strings if all(div != 0 for div in dividers[val]) ]
    output.write(formatOutput(1, ''))

    found_cpt = 0
    val_cpt = 0
    val_max = pow(2, n-2)
    answer = ''

    while found_cpt < j:
        seq = '1' + str(bin(val_cpt)[2:].zfill(n-2)) + '1'
        divs, has_prime = getDivs(seq)
        if not has_prime:
            answer += seq
            for div in divs:
                answer += ' ' + str(div)
            answer += '\n'
            found_cpt += 1
        val_cpt += 1

    output.write(answer)


file = open(sys.argv[1])
output = open('output.txt', 'w')
nTests = int(file.readline())

testNb = 1
for line in itertools.islice(file, 0, nTests+1):     
    solveProblem(line)
    testNb += 1
