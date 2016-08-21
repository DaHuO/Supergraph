def sub(S, possible_S):
    SA = list(S)
    PSA = list(possible_S)
    d = 0
    for i in range(0, len(SA)):
        if SA[i] == '?':
            SA[i] = PSA[d]
            d += 1
    #print(S + " " + possible_C + " " + "".join(SA))
    return int("".join(SA))


# Input files
fin = open('score.in', 'r')
fout = open('score.out', 'w')

T = int(fin.readline())

for t in range(0, T):
    S = fin.readline().split()
    C = S[0]
    J = S[1]

    C_missing = C.count('?')
    J_missing = J.count('?')

    possible_Cs = pow(10, C_missing)
    possible_Js = pow(10, J_missing)

    minDiff = pow(10, 20)
    minC = 0
    mintJ = 0

    for pc in range(0, possible_Cs):
        possible_C = str(pc).zfill(C_missing)
        c = sub(C, possible_C)

        for pj in range(0, possible_Js):
            possible_J = str(pj).zfill(J_missing)
            j = sub(J, possible_J)

            if abs(c - j) < minDiff:
                minDiff = abs(c - j)
                minC = c
                minJ = j

    #print(str(minC).zfill(len(C)) + " " + str(minJ).zfill(len(J)))
    fout.write("Case #" + str(t+1) + ": " + str(minC).zfill(len(C)) + " " + str(minJ).zfill(len(J)) + "\n")

# Output files
fin.close()
fout.close()