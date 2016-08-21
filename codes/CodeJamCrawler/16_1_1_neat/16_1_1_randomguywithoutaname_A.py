## Problem A

def probA(S):
    result = S[0]
    for c in S[1:]:
        if c >= result[0]:
            result = c + result
        else:
            result = result + c
    return result

for i in range(1, int(raw_input()) + 1):
    print "Case #%d: %s" % (i, probA(raw_input()))

