import sys

def do(s):
    cnt = 1
    prev = s[0]
    for i in xrange(1, len(s)):
        if s[i] != prev:
            cnt += 1
            prev = s[i]

    if s[0] == '+':
        cnt = (cnt >> 1) << 1
    elif s[0] == '-':
        cnt = (((cnt - 1) >> 1) << 1) + 1

    return cnt

def main():
    t = int(sys.stdin.readline())
    for i in xrange(t):
        print "Case #{0}: {1}".format(i + 1, do(list(sys.stdin.readline().strip())))

if __name__ == '__main__':
    main()
