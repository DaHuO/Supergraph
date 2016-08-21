import sys

def main():
    n_tests = int(sys.stdin.readline()) # unused
    line_no = 0
    for line in sys.stdin:
        line_no += 1
        n = int(line)
        current = 0
        seen = set()
        if n == 0:
            print 'Case #{}: INSOMNIA'.format(line_no)
        else:
            while len(seen) < 10:
                current += n
                seen |= set(str(current))
                if len(seen) == 10:
                    print 'Case #{}: {}'.format(line_no, current)


main()
