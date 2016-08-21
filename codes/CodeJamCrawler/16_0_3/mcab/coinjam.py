import math

def factor(n):
    factor = 0
    if n % 2 == 0:
        return 2
    else:
        _ = 3
        while (_ < long(math.floor(math.sqrt(n))) + 1):
            if _ > 2**16:
                return 0
            if n % _ == 0:
                return _
            _ += 2
    return 0

def main():
    outFile = open('coinjamout.txt', 'w')
    outFile.write('Case #1: \n')
    # 32769 to 65536 (inclusive) is 1000000000000001 to 1111111111111111
    # larger is harder...
    #for _ in xrange(32769, 65536):
    _ = long(2147483649)
    while _ < long(4294967295):
        if '{0:032b}'.format(_)[-1] == '1':
            valid = True
            factors = []
            for fac in xrange(2, 11):
                potentialFactor = factor(long('{0:032b}'.format(_), fac))
                if potentialFactor == 0:
                    valid = False
                    break
                else:
                    factors.append(potentialFactor)
            if valid == True:
                outFile.write('{0:032b}'.format(_) + ' ' + ' '.join(map(str, factors)) + '\n')
        _ += 2
    outFile.close()

if __name__ == "__main__":
    main()