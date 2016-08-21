import sys

digits = set([0,1,2,3,4,5,6,7,8,9])

def lastNumber(n, digits_counted, base=1):
    if n == 0:
        return "INSOMNIA"
    if digits_counted == digits:
        return n*(base -1)
    n_window = n*base
    while n_window != 0:
        digits_counted.add(n_window % 10)
        n_window /= 10
    return lastNumber(n, digits_counted, base +1)


def inputDissect(s):
    lines = s.split("\n")
    inputCnt = int(lines.pop(0))
    for offset in xrange(inputCnt):
        y = lastNumber(int(lines[offset]), set([]))
        print "Case #%d:" % (offset + 1), y


inputDissect(open(sys.argv[1], "r").read())
