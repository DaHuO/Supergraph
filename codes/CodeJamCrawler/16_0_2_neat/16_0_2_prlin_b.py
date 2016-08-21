import sys

def handle_case(line):
    cakes = line.strip()

    def check(cakes):
        return cakes == '+'*len(cakes)

    def swap(cakes):
        new=[]
        for cake in cakes:
            if cake == '+':
                new.append('-')
            else:
                new.append('+')
        return new

    if check(cakes):
        return 0

    # filp from right to left whenever we see a '-'
    flip_count = 0
    while True:
        idx = cakes.rfind('-')
        if idx != -1:
            cakes = ''.join(list(swap(cakes[:idx+1]))+list(cakes[idx+2:]))
            flip_count += 1
        else:
            return flip_count


if __name__ == '__main__':
    cases = int(sys.stdin.readline().strip())

    for i in xrange(1, cases+1):
        line = sys.stdin.readline().strip()
        answer = handle_case(line)
        print "Case #{}: {}".format(i, answer)
