def check(z):
    binstr = bin(z)[2:]
    for i in xrange(2, 11):
        num = 0
        w = 1
        for j in xrange(0, len(binstr)):
            if binstr[len(binstr) - 1 - j] == '1':
                num += w
            w *= i
        if num % (i+1) != 0:
            return False
    return True

def main():
    n = 32
    J = 500
    print "Case#1:"
    z = (1<<n) / 3 * 3
    for i in xrange(0, J):
        while check(z) == False:
            z -= 6
        print "%s 3 4 5 6 7 8 9 10 11" % (bin(z)[2:])
        z -= 6


if __name__  == '__main__':
    main()
