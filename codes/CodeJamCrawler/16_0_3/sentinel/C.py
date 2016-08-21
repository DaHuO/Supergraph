import sys
import math

primes = []
def getDivisor(num):
    if num in primes:
        return None
    divisor = 2
    while (divisor <= math.sqrt(num)):
        if num % divisor == 0:
            return divisor
        divisor = divisor+1
    primes.append(num)
    return None

def getNextBinary(strLen):
    val = 0
    binVal = ''
    while len(binVal) <= strLen:
        binVal = bin(val).replace('0b', '');
        while len(binVal) < strLen -2:
            binVal = '0{}'.format(binVal)
        yield '1{}1'.format(binVal)
        val = val +1

def processRecord(n, j):
    results = []
    gen = getNextBinary(n)
    bases = [x+2 for x in xrange(9)]
    while len(results) < j:
        binary = next(gen)
        line = binary
        append = True
        for base in bases:
            num = int(binary, base)
            # print "trying {} in base {} as {}".format(binary, base, num)
            divisor = getDivisor(num)
            if not divisor:
                append = False
                # print "failed"
                break
            else:
                line = "{} {}".format(line, divisor)
        if append:
            results.append(line)
    return results

def processLine(fp, x):
    inStr = fp.readline()
    n, j = inStr.split(' ')
    n, j = [int(n), int(j)]
    results = processRecord(n, j)
    print 'Case #{}'.format(x)
    print "\n".join(results)

def main():
    filename = sys.argv[1]

    try:
        fp = open(filename)
        records = int(fp.readline())
        for x in xrange(records):
            processLine(fp, x+1)
        fp.close()
    except Exception as e:
        print e

if __name__ == '__main__':
    main()
