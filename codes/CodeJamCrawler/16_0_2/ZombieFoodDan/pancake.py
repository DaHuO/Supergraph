import sys, os

def main():
    t = int(raw_input())  # read a line with a single integer
    #print t
    inputs = []
    for i in xrange(1, t + 1):
        n = str(raw_input())
        inputs.append(n)
        #print n
        #n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        #print "Case #{}: {} {}".format(i, n + m, n * m)
        # check out .format's specification for more formatting options

    #ubound = 1000000

    case = 0
    for stack in inputs:
        case += 1
        #k = 1
        flips = 0
        test = []
        while '-' in stack:
            o = ''
            for s in stack:
                if s != o:
                    if s == '-':
                        test.append(1)
                    else:
                        test.append(0)
                    o = s

            while test[-1] == 0:
                del test[-1]

            break

        flips = len(test)
        print 'Case #%s: %s' % (case, flips)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print e.message
