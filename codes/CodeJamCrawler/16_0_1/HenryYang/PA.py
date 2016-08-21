import sys
input = file(sys.argv[1])

def solve(s):
    if s == 0:
        return 'INSOMNIA'
    ct = [0] * 10
    n = 1
    while True:
        x = n * s
        while x > 0:
            ct[x%10] = 1
            x /= 10
        if sum(ct) == 10:
            return n * s
        n += 1

for case in range(int(input.readline())):
    value = int(input.readline())
    print "Case #%d: %s" % (case+1, solve(value))
