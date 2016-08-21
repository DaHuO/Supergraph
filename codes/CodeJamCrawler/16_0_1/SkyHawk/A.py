import sys

T = int(raw_input())
for case_idx in xrange(1, T+1):
    sys.stdout.write("Case #{}: ".format(case_idx))
    n = int(raw_input())
    if n == 0:
        print "INSOMNIA"
        continue

    letters = set()
    value = n
    for i in xrange(1, 1000000000):
        string = str(value * i)
        letters.update(string)
        if len(letters) == 10:
            print string
            break
