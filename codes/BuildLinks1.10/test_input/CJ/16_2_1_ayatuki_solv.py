import sys
data = [v.rstrip() for v in open(sys.argv[1])]
T = data[0]
dataset = data[1:]

def minus(S, val):
    for c in val:
        if c not in S or S[c] == 0:
            return None
        S[c] -= 1
        if S[c] == 0:
            del S[c]
    return S

def ToAlp(n):
    NUM = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE",
         "SIX", "SEVEN", "EIGHT", "NINE"]
    return NUM[n]

def solv(S, pn):
#    print(str(S), str(pn))
    if len(S) == 0:
        return pn
    for n in range(10):
        newS = minus(S.copy(), ToAlp(n))
        if newS is None:
            continue
        npn = solv(newS, pn + [n])
        if npn is not None:
            return npn


def ToMap(S):
    result = {}
    for c in S:
        result[c] = result.get(c, 0) + 1
    return result

for i in range(int(T)):
    result = solv(ToMap(dataset.pop(0)), [])
    print("Case #{0}: {1}".format(i+1, ''.join([str(v) for v in sorted(result)])))
