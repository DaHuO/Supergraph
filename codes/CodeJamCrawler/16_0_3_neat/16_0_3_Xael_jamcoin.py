import math

def inbase(a, base):
    return int(str(a), base)

def divisor(a):
    if a % 2 == 0:
        return 2
    d = 3
    while d <= math.sqrt(a):
        if a % d == 0:
            return d
        d += 2
    return a

def nextjam(jam, N):
    core = int((jam - 1 - (10 ** N)) / 10)
    q = int(str(core), 2) + 1
    b = int('{0:b}'.format(q))
    return (b * 10) + 1 + (10 ** N)

fi = open('A-large.in', 'r')
fo = open('output.txt', 'w')

T = int(fi.readline())

for t in range(T):
    print('Case #{0}:'.format(t+1))
    fo.write('Case #{0}:\n'.format(t+1))
    line = fi.readline()
    [N, J] = map(int, list(line.split(' ')))
    jam = 10 ** (N - 1) + 1
    curpos = 1
    minpos = 0
    maxpos = N - 1
        
    while J > 0:
        k = [0] * 9
        dk = [0] * 9
        for b in range(2, 11):
            isPrime = False
            k[b-2] = inbase(jam, b)
            dk[b-2] = divisor(k[b-2])
            if dk[b-2] == k[b-2]:
                isPrime = True
                break
            
        if isPrime == False:
            #print(k)
            print(str(jam), ' '.join(map(str, dk)))
            fo.write('{0} {1}\n'.format(str(jam), ' '.join(map(str, dk))))
            J -= 1

        jam = nextjam(jam, N - 1)

fi.close()
fo.close()
