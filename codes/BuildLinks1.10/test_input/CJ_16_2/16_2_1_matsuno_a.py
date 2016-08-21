import sys

ALPHA = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
FEATURE = ["Z", "O", "W", "T", "U", "F", "X", "S", "G", "I"]

def do(s):
    cnt = [0] * 10
    for c in s:
        for i in [0,2,4,6,8]:
            if c == FEATURE[i]:
                cnt[i] += 1

    a = list(s)
    for i in [0,2,4,6,8]:
        for j in xrange(cnt[i]):
            for c in ALPHA[i]:
                a.remove(c)

    for c in a:
        for i in [1,3,5,7]:
            if c == FEATURE[i]:
                cnt[i] += 1

    for i in [1,3,5,7]:
        for j in xrange(cnt[i]):
            for c in ALPHA[i]:
                a.remove(c)

    for c in a:
        for i in [9]:
            if c == FEATURE[i]:
                cnt[i] += 1

    r = []
    for i,n in enumerate(cnt):
        for j in range(n):
            r.append(str(i))

    return ''.join(r)

def main():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        print "Case #{0}: {1}".format(t + 1, do(sys.stdin.readline().strip()))

if __name__ == '__main__':
    main()
