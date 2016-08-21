# https://code.google.com/codejam/contest/6254486/dashboard#s=p0
import sys

def run(n0):
    if (n0 == 0):
        return 'INSOMNIA'
        # TODO Any other cases that don't terminate?
    digits = set()
    i = 0
    while len(digits) < 10:
        i += 1
        n = n0 * i
        digits |= set(list(str(n)))
        #print digits, n
    return n

def parse(lines):
    return int(lines.pop(0))

def main(infile):
    lines = infile.readlines()
    count = int(lines.pop(0))
    cases = (parse(lines) for case in range(count))
    output = (run(case) for case in cases)
    for i, result in enumerate(output):
        print "Case #%d: %s" % (i + 1, result)

if __name__=='__main__':
    main(sys.stdin)
