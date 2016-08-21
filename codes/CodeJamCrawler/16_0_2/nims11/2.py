T = input()
Z = 1
def ans(x):
    print "Case #%d: %s" % (Z, str(x))

def solve(S):
    if S == len(S)*'+':
        return 0
    ret = 0
    idx = 0
    while S[idx] == '+':
        idx += 1
    if idx > 0:
        ret += 1
        S = '-'*len(S[:idx][::-1]) + S[idx:] 
    ret += 1
    S = S[::-1]
    S = ''.join(['-' if c is '+' else '+' for c in S])
    for idx in range(len(S)):
        if len(S[idx:])*'+' == S[idx:]:
            return ret + solve(S[:idx])

while Z <= T:
    S = raw_input()
    for idx in range(len(S)+1):
        if len(S[idx:])*'+' == S[idx:]:
            ans(solve(S[:idx]))
            break
    Z += 1
