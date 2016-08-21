ifile = open('A-large.in', 'r')
ofile = open('A-large.out', 'w')

TC = int(ifile.readline())

for tc in range(1, TC + 1, 1):
    S = ifile.readline()
    start = S[0]
    last = S[0]
    result = [S[0]]
    for i in range(1, len(S)):
        if S[i] <= last:
            result.append(S[i])
            last = S[i]
        elif S[i] > last:
            if S[i] >= start:
                result.insert(0, S[i])
                start = S[i]
            else:
                result.append(S[i])
                last = S[i]
    ofile.write("Case #{0}: {1}".format(tc, ''.join(result)))
