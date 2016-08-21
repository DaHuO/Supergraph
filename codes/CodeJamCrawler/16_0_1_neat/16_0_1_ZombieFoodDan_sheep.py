import sys, os

def main():
    t = int(raw_input())  # read a line with a single integer
    #print t
    inputs = []
    for i in xrange(1, t + 1):
        n = int(raw_input())
        inputs.append(n)
        #print n
        #n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        #print "Case #{}: {} {}".format(i, n + m, n * m)
        # check out .format's specification for more formatting options

    ubound = 1000000

    case = 0
    for n in inputs:
        case += 1
        k = 1
        found = False
        seen = []
        while not found:
            if k > ubound:
                break
            o = k * n
            for s in str(o):
                if s not in seen:
                    seen.append(s)

            if len(seen) > 9:
                break
            k = k + 1

        if k <= ubound:
            print 'Case #%s: %s' % (case, o)
        else:
            print 'Case #%s: %s' % (case, "INSOMNIA")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print e.message
