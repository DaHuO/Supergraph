import itertools

def testprime(n):
    for i in range(2, int(n**(1/2))+1):
        if not n % i: return i
    return 0


def tryjam(S):
    ret = ''
    for base in range(2, 11):
        seqB = int(S, base)
        t = testprime(seqB)
        if not t: return ''
        else: ret += str(t) + ' '
    return ret


def func(N=16, J=50):
    C = 0
    good = []
    for seq in itertools.product("01", repeat=N-2):
        S = '1' + ''.join(seq) + '1'
        if S[0] == S[-1] == '1':
            s = tryjam(S).strip()
            if s:
                C+=1
                good += [(S, s)]
                if C >= J: return good

good = func()
f='outfl3.txt'
with open(f, 'w') as of:
    of.write('Case #1:\n')
    for (n,ds) in good:
        of.write(n+' '+ds+'\n')

