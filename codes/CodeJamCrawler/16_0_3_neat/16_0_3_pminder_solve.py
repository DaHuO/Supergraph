import pyprimes.factors

N = 16
J = 50


def sbin(x):
    return bin(x)[2:]

def isJamCoin(s):
    bases = [i for i in range(2, 11)]
    ff = []

    for b in bases:
        n = int(s, b)
        f = pyprimes.factors.factorise(n)
        if f == [n]:
            return []
        ff.append(str(f[0]))

    return ff
        

x = 0
print "Case #1:"
# while len(sbin(x)) < 5:
while J != 0:

    s ='1' + sbin(x).zfill(N-2) + '1'

    dividers = isJamCoin(s)
    if dividers != []:
        print "{} ".format(s) + " ".join(dividers)
        J -= 1

    x += 1

