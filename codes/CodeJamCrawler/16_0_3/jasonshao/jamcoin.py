"""primes = set()
lim = 100000
a = []
for i in range(lim):
    a.append(True)


for i in range(2, lim):
    if a[i] == True:
        primes.add(i)
        j = 2*i
        while j < lim:
            a[j] = False
            j += i

"""
def convert(a):
    b = []
    while a != 0:
        b.append(a % 2)
        a /= 2
    return b

def convert2(a, base):
    a = a[::-1]
    ret = 0
    for i in range(len(a)):
        ret += int(a[i]) * (base ** i)
    return ret
"""

ans = {}
for poss in range(2**31 + 1, 2 **32 - 1, 2):
    l = convert(poss)
    divis = []
    for base in range(2, 11):
        for prime in primes:
            mod = 0
            for i in range(len(l)):
                if l[i] == 1:
                    mod += pow(base, i, prime)
                    mod %= prime
            if prime != poss and mod == 0:
                divis.append(prime)
                break
    if len(divis) == 9:
        l.reverse()
        l = map(str, l)
        ans[''.join(l)] = divis
        print ''.join(l), divis
    if len(ans) == 500:
        break
        """

print "Case #1:"
with open('hackcoin', 'r') as f:
    for i in f.readlines():
        k = map(int, i.replace('\'', '', 20).replace('[', '', 20).replace(']', '', 20).replace(',', '', 20).split())
        ans = str(k[0])
        div = k[1:]
        print ans,
        for h in div:
            print h,
        print
