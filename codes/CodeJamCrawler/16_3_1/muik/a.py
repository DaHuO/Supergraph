import fileinput
f = fileinput.input()
T = int(f.readline())

def solve(N, P):
    steps = []
    senators = [[chr(ord('A')+i), n] for i, n in enumerate(P)]
    remaining = sum(P)
    while remaining >= 1:
        senators = sorted(senators, key=lambda x: x[1], reverse=True)
        max = senators[0][1]
        if (100.0 * max / remaining) > 50.0:
            print("error!!!")
            exit(1)
        if remaining <= 2:
            step = ''.join([s[0] for s in senators if s[1] > 0])
        else:
            step = senators[0][0]
            senators[0][1] -= 1
            if remaining != 3 and senators[1][1] == max:
                step += senators[1][0]
                senators[1][1] -= 1
        steps.append(step)
        remaining -= len(step)
    return ' '.join(steps)

for case in range(1,T+1):
    N = f.readline().strip()
    P = [int(p) for p in f.readline().strip().split(' ')]
    print "Case #%d: %s" % (case, solve(N, P))
