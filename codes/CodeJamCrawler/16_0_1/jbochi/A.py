import sys

def output(n):
    not_seen = set(range(0, 10))
    for i in range(1, 1000):
        number = i * n
        not_seen -= set(map(int, str(number)))
        #print set(str(number))
        if len(not_seen) == 0:
            return number
    return "INSOMNIA"

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        n = int(sys.stdin.readline())
        answer = output(n)
        print "Case #%d: %s" % (t + 1, answer)
