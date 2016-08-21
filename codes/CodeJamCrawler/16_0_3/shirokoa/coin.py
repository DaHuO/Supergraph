import sys
import random
import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return dict(test=False,example=2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return dict(test=False,example=i)
    return dict(test=True)

T = input()
#print(T )

N,J = (int(s) for s in input().split())
#print(N)
#print(J)

#fho = open(sys.argv[1],'w')
fho = sys.stdout

print('Case #1:',file=fho)

ncoins = 0
while 1:

    def getit(coin):
        N = len(coin)
        def interp(base):
            k = 0
            for i in range(N):
                c = coin[N-(i+1)]
                b = base**i
                incr = b*int(c)
                #print(i,c, b)
                k += incr
            return k

        T = []
        for base in range(2,10+1):
            K = interp(base=base)
            t = is_prime(K)
            if t['test']:
                return dict(test=False)
            else:
                T += [str(t['example'])]
        return dict(test=True,examples=' '.join(T))

    def generate():
        c = ['1']
        for i in range(N-2):
            c += ['0' if random.uniform(0,1) < 0.5 else '1']
        c += ['1']
        return ''.join(c)

    coin = generate()

    t = getit(coin=coin)
    if t['test']:
        print(coin,t['examples'])
        ncoins += 1
        if ncoins == J: break



