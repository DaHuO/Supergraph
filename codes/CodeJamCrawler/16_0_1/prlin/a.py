import sys


want = range(10)

def handle_case(line):
    N = line.strip()
    N = int(N)

    if N == 0:
        return "INSOMNIA"
    seen = set()
    def check_set(s):
        return want == sorted(list(s))
    i = 1
    while True:
        num = N*i
        i += 1
        for d in str(num):
            seen.add(int(d))
        if check_set(seen):
            return num

if __name__ == '__main__':
    cases = int(sys.stdin.readline().strip())

    for i in xrange(1, cases+1):
        line = sys.stdin.readline().strip()
        answer = handle_case(line)
        print "Case #{}: {}".format(i, answer)
