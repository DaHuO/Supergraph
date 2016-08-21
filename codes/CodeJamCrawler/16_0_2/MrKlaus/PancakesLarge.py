def flipstack(s):
    rs = s[::-1]
    fs = rs.replace("1", "2").replace("0", "1").replace("2", "0")
    return fs

def CalcMinimum(pancakeStack):
    P = pancakeStack.replace("-","0").replace("+","1")
    M = 0

    for i in range(len(P)-1):
        CurVal = P[i]
        NextVal = P[i+1]
        if CurVal != NextVal:
            topN = i+1
            ps = P[:topN]
            F = flipstack(ps)
            M = M + 1
            P = F + P[topN:]

    if P[0] == '0':
        P = flipstack(P)
        M = M + 1

    return M

BLargeFile = 'B-large.in'

f = open(BLargeFile, 'r')
T = int(f.readline())

o = open('B-large-output.txt','w')

for j in range(T):
    S = str(f.readline().strip())
    A = CalcMinimum(str(S))

    o.write('Case #' + str(j+1) + ': ' + str(A) + '\n')

f.close()
o.close()


