N=32
J=500

def next_num(N):
    for i in xrange(2**(N-1)+1, 2**N, 2):
        yield "{0:b}".format(i)

def get_witness(n):
    for i in xrange(2, 1000): #int(n**0.5)+2):
        if n%i == 0:
            return i
    return None

def check(x):
    witness = []
    for base in range(2, 11):
        n = int(x, base)
        w = get_witness(n)
        if not w:
            #print "fail at", base
            return None
        witness.append(w)
    return witness

print "Case #1:"
for n in next_num(N):
    res = check(n)
    if res:
        print n, " ".join(str(x) for x in res)
        J-=1
        if not J:
            break
        

