import sys

def do(inp):
    cnt = 0
    inp = list(inp)
    while len(inp) > 0:
        while len(inp) > 0 and inp[-1] == '+':
            del inp[-1]
        if len(inp) == 0:
            break

        if inp[0] == '+':
            for i in range(len(inp)):
                if inp[i] == '+':
                    inp[i] = '-'
                else:
                    break
            cnt += 1

        for i in range(len(inp)):
            if inp[i] == '+':
                inp[i] = '-'
            else:
                inp[i] = '+'
        cnt += 1

    return cnt

N = int(sys.stdin.readline())
for i in range(N):
    inp = sys.stdin.readline().strip()
    r = do(inp)
    print 'Case #%d: %s' % (i + 1, r)

