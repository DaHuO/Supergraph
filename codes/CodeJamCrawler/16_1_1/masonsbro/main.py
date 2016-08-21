def findBest(S):
    if len(S) == 0:
        return S
    maxletter = max(S)
    firstOccurrence = S.index(maxletter)
    return maxletter*S.count(maxletter) + findBest(S[:firstOccurrence]) + "".join([c if c != maxletter else '' for c in S[firstOccurrence:]])

T = int(raw_input())

for t in range(1,T+1):
    S = raw_input()
    print "Case #%d: %s" % (t, findBest(S))
