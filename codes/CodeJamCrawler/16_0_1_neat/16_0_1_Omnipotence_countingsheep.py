import sys


def main(argv):
    # read in file
    input_file = argv[0]
    f = open(input_file)
    T = int(f.readline())
    for i in xrange(1, T+1):
        case = int(f.readline())
        print "Case #%s: %s" % (i, calculate(case))


def calculate(case):
    if case:
        n = case
        digits_to_see = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        while True:
            digits_to_see -= set(str(n))
            if len(digits_to_see) == 0:
                return n
            n += case
    else:
        return "INSOMNIA"

if __name__ == '__main__':
    main(sys.argv[1:])
