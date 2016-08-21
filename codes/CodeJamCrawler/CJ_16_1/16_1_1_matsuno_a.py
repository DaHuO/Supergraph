import sys
from collections import deque

def do(s):
    r = deque()
    pivot = ''
    for i, c in enumerate(s):
        if i == 0:
            pivot = c
            r.append(c)
            continue
        if c < pivot:
            r.append(c)
        else:
            r.appendleft(c)
            pivot = c

    return ''.join(list(r))

def main():
    T = int(sys.stdin.readline())
    for t in range(T):
        answer = do(sys.stdin.readline().strip())
        print "Case #{0}: {1}".format(t + 1, answer)

if __name__ == '__main__':
    main()
