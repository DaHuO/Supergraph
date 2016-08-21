
# GCJ 2016 Qual A jeremy.holman@gmail.com

T = int(raw_input())

def do_counting(N):
    idx = 0
    seen = [False] * 10
    while False in seen:
        idx += 1
        for digit in list(str(N*idx)):
            seen[int(digit)] = True
    return N*idx

for t in xrange(T):
    X = int(raw_input())
    if X == 0:
        print "Case #%i: INSOMNIA" % (t+1)
    else:
        print "Case #%i: %i" % (t+1, do_counting(X))
