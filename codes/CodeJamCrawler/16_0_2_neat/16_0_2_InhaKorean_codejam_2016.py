FILE_PATH = 'C:\\codejam\\'
FILE_NAME = 'B-large'

f = open(FILE_PATH + FILE_NAME + '.in', 'r')
o = open(FILE_PATH + FILE_NAME + '.out', 'w')
 
def case_result(case) :
    S = f.readline()
    if S[-1] == '\n' :
        S = S[:-1]

    n = len(S)

    L1 = [0]*n
    L2 = [0]*n
    if S[0] == '-' :
        L1[0] = 1
    else :
        L2[0] = 1

    for i in range(1, n) :
        if S[i] == '+'  :
            L1[i] = L1[i-1]
            L2[i] = L1[i-1] + 1
        else :
            L1[i] = L2[i-1] + 1
            L2[i] = L2[i-1]

    return str(L1[-1])

T = int(f.readline())
for case in range(1, T+1) :
    o.write('Case #'+str(case)+': '+case_result(case)+'\n')
 
f.close()
o.close()
 