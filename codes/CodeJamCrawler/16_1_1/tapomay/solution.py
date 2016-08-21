N = int(input())

def lastword(S):
    ret = S[0]
    for c in S[1:]:
        if c >= ret[0]:
            ret = c + ret
        else:
            ret = ret + c
    return ret

for i in range(1, N+1):
    M = str(input())
    lw = lastword(M)
    print('Case #' + str(i) + ': ' + str(lw))
