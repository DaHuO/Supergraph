import random

def insomnia(N):
    inso = False
    if N == 0:
        inso = True
    return inso

fo = open('aoutputlarge.txt','w')
fi = open('A-large.in','r')
T = int(fi.readline())
#T = 10000000
for c in range(1, T+1):
    print str(c) + ' of ' + str(T)
    N = int(fi.readline())
    #N = random.randint(1,10000000)
    if insomnia(N):
        fo.write('Case #' + str(c) + ': INSOMNIA\n')
    else:
        k = 0
        digits = [0] * 10
        while sum(digits) < 10:
            k = k + 1
            s = str(k*N)
            for l in s:
                digits[int(l)] = 1
        fo.write('Case #' + str(c) + ': '+ str(k*N) + '\n')
