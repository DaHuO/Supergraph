import sys

# get all cases and sort them
def get_final(s, N):
    for i in xrange(N):
        next = ""
        for j in s:
            if j == "R":
                next += "RS"
            elif j == "S":
                next += "PS"
            elif j == "P":
                next += "PR"
        s = next
    assert len(s) == 2**N
    return sort_l(s, N)

def sort_l(s, N):
    for i in xrange(0, N):
        for j in xrange(0, len(s), 2**(i+1)):
            substrA = s[j:j+2**i]
            substrB = s[j+2**i:j+2*(2**i)]
            assert len(substrA) == len(substrB)
            if substrA > substrB:
                s = s[:j] + substrB + substrA + s[j+2*(2**i):]
    return s 

answers = dict()
for N in xrange(1,13+1):
    for s in ["R","P","S"]:
        foo = get_final(s, N)
        R = foo.count("R")
        P = foo.count("P")
        S = foo.count("S")
        if (R,P,S) in answers:
            if foo < answers[(R,P,S)]:
                answers[(R,P,S)] = foo
        else:
            answers[(R,P,S)] = foo

with open(sys.argv[1]) as f:
    lines = f.readlines()

T = int(lines[0],10)
for tt, l in enumerate(lines[1:]):
    N, R, P, S = tuple(map(int, l.strip().split(" ")))
    if (R,P,S) in answers:
        print ("Case #%d:" % (tt+1)), answers[(R,P,S)]
    else:
        print ("Case #%d:" % (tt+1)), "IMPOSSIBLE"

        

