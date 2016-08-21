import sys

def main():
    inputs = next(sys.stdin)

    case = 0
    for line in sys.stdin:
        case += 1
        count = 0

        pancakes = list(line[:-1])

        pancakes.append('+')

        for i in xrange(1, len(pancakes)):
            if pancakes[i] != pancakes[i - 1]:
                count += 1

        print "Case #{}: {}".format(case, count)




if __name__ == '__main__':
    exit(main())