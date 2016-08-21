import string

UPPER_CASE = string.ascii_uppercase

ifile = open('A-large.in', 'r')
ofile = open('A-large.out', 'w')
# ifile = open('A.test.in', 'r')
# ofile = open('A.test.out', 'w')

TC = int(ifile.readline())

def check_half(P):
    T = sum(P)
    for i in P:
        if i <0 or i > T/2:
            return False
    return True

for tc in range(1, TC+1, 1):
    print("Case #{0}".format(tc))

    N = int(ifile.readline()) # number parties
    P = [int(i) for i in ifile.readline().strip().split()] # senators in each party
    print N, P

    T = sum(P)
    
    steps = []
    while T > 0:
        t = 0
        
        for i in xrange(N):
            for j in xrange(N):
                if t > 0:
                    break
                _P = list(P)
                _P[i] -= 1
                _P[j] -= 1
                if check_half(_P):
                    P[i] -= 1
                    P[j] -= 1
                    t += 2
                    steps.append(UPPER_CASE[i])
                    steps.append(UPPER_CASE[j])
            if t > 0:
                break

        if t == 0:
            for i in xrange(N):
                _P = list(P)
                _P[i] -= 1
                if check_half(_P):
                    P[i] -= 1
                    t += 1
                    steps.append(UPPER_CASE[i])
        if t == 0:
            exit(1)
        T -= t
        steps.append(' ')

    ans = ''.join(steps)

    ofile.write("Case #{0}: {1}\n".format(tc, ans))
