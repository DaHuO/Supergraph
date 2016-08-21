from math import sqrt, ceil

inputName = 'C-coinjam-practice'

# Take input
infile = open(inputName + '.in', 'r')
lines = infile.readlines()
infile.close()

outfile = open(inputName + '-out.txt', 'w')
outfile.write('Case #1:')

# Prime-checking function

# For small numbers, could have a precompiled list of primes to check, maybe
# but still need a divisor

primesBelow1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def getDivisor(myNum):
    # naive approach, trial division
    for i in range(len(primesBelow1000)):
        testPrime = primesBelow1000[i]
        if testPrime ** 2 > myNum:
            return 0 # number less than 1000 and not prime
        elif myNum % testPrime == 0:
            return testPrime
    # If no divisors in first 1000 primes, continue trial division
    for i in range(primesBelow1000[len(primesBelow1000)-1], ceil(sqrt(myNum))):
        if myNum % i == 0:
            return i
    return 0  # prime

# Functions for getting binary strings back from ints in a given base
def digit_to_char(digit):
    if digit < 10: return chr(ord('0') + digit)
    else: return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number,base)
    else:
        (d,m) = divmod(number,base)
        if d:
            return str_base(d,base) + digit_to_char(m)
        else:
            return digit_to_char(m)

for x, line in enumerate(lines):
    if x == 0:
        numTests = int(line)
    else:
        (N, J) = line.split()
        N = int(N)
        J = int(J)
        print(N)
        print(J)

        resultCount = 0
        seedNum = [0]*N
        # Restrictions: first and last digits are 1
        seedNum[0] = 1
        seedNum[N-1] = 1
        num = int(''.join(str(x) for x in seedNum), 2)
        print(num)

        while resultCount < J:
            print(seedNum)
            writeResult = True
            resultString = ''.join(str(x) for x in seedNum)
            for base in range(2, 11):
                numInBase = 0

                # Convert to the given base
                for j in range(len(seedNum)):

                    numInBase += int(seedNum[j]) * base ** (N-j-1)
                    print(numInBase)

                # Check primality
                primeResult = getDivisor(numInBase)
                if primeResult == 0:
                    writeResult = False
                    break
                else:
                    # Append this divisor
                    resultString += ' ' + str(primeResult)

            # Write output if successful
            if writeResult:
                resultCount += 1
                print(resultString)
                outfile.write('\n' + resultString)

            # Increment seedNum by two (keeping last digit as 1
            num += 2
            seedNum = list(str_base(num, 2))
            if len(seedNum) < N:
                # add padding zeroes
                seedNum = [0]*(N-len(seedNum)-1) + seedNum



outfile.close()
