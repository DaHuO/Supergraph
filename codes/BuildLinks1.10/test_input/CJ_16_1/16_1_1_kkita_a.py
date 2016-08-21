#!/usr/bin/python

T = int(input())
result = []
for cases in range(0,T):
    Q = input()
    S = Q[0]
    R = "".join(Q[1:])
    for letter in R:
        if (letter < S[0]):
            S = S + letter
        else:
            S = letter + S
    result.append((cases+1, "".join(S)))

for (x,y) in result:
    print("Case #%d: %s" % (x,y))
