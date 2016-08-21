import sys

def compute(m):
    n = m
    if n == 0:
        print 'INSOMNIA'
        return
    remaining = [0 ,1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        #print 'Testing with n = ' + str(n)
        digits = [int(i) for i in str(n)]
        for digit in digits:
            try:
                remaining.remove(digit)
            except:
                continue
        if len(remaining) == 0:
            print n
            break
        n = n + m

with open(sys.argv[1], "r") as f:
    skip = True
    i = 1
    for line in f:
        if not skip:
            print 'Case #' + str(i) + ':',
            i = i + 1
            compute(int(line.strip()))
        else:
            skip = False
