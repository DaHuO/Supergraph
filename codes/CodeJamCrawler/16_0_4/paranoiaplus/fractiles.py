num = int(raw_input())

def solve(win):
    arr = map(int, win.split())
    s = arr[2]
    seq = [x for x in range(1, s+1)]
    return ' '.join(map(str, seq))

for i in xrange(1, num+1):
    print "Case #{}: {}".format(i, solve(raw_input()))
