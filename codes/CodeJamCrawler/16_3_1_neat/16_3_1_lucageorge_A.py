f = open("OutputLarge.txt", "w")

alphabet = map(chr, range(65, 91))

def senate_not_empty(lista):
    for e in lista:
        if e[0] != 0:
            return True
    return False

i = 0
for S in open("A-large.in", "r"):
    S = [int(c) for c in S[:-1].split()]
    if len(S) > 1:
        S = [list(e) for e in zip(S, alphabet)]
        
        ans = []
        while senate_not_empty(S):
            S = sorted(S, key = lambda e : e[0], reverse = True)
            otherPartiesSum = sum([c[0] for c in S[1:]])
            if otherPartiesSum > S[0][0]:
                if len(S) > 2:
                    S[0][0] -= 1
                    ans.append(S[0][1])
                else:
                    if S[0][0] == S[1][0]:
                        S[0][0] -= 1
                        S[1][0] -= 1
                        ans.append(S[0][1] + S[1][1])
                    else:
                        S[0][0] -= 1
                        ans.append(S[0][1])
            elif otherPartiesSum == S[0][0]:
                    S[0][0] -= 1
                    S[1][0] -= 1
                    ans.append(S[0][1] + S[1][1])
        ans = "Case #" + str(i+1) + ": " + " ".join(ans) + "\n"
        f.write(ans)
        i += 1
f.close()
