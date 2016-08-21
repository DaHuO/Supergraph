## Problem A

def probA(N):
    if N == 0:
        return 'INSOMNIA'
    i = 0
    seen = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    while len(seen) > 0:
        i += 1
        for c in str(i*N):
            if c in seen:
                seen.remove(c)
    return str(i*N)

for i in range(1, int(raw_input()) + 1):
    print "Case #%d: %s" % (i, probA(int(raw_input())))

