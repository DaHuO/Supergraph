import math
def FUN(C, J):
    CL = [d for d in C]
    JL = [d for d in J]    
    CBiger = True
    idx = 0
    lastQI = 0
    for i in xrange(len(CL)):
        if CL[i] == JL[i]:
            if CL[i] == '?':
                CL[i] = '0'
                JL[i] = '0'
                lastQI += 1
        elif CL[i] == '?':
            CL[i] = JL[i]
            lastQI += 1
        elif JL[i] == '?':
            JL[i] = CL[i]
            lastQI += 1
        elif int(CL[i]) < int(JL[i]):
            CBiger = False
            idx = i+1
            break
        else:
            idx = i+1
            break
    special = True and lastQI < len(CL) - 1
    for i in xrange(idx, len(CL)):
        if CL[i] == '?' or JL[i] == '?':
            special = False
            break
    if special:
        Cpartial = int(C[lastQI+1:])
        Jpartial = int(C[lastQI+1:])
        if Cpartial - Jpartial > (pow(10,len(CL) - lastQI - 1)/2):
            if C[lastQI] == '?' and J[lastQI] == '?':
                CL[lastQI] = '0'
                JL[lastQI] = '1'
            elif C[lastQI] == '?':
                CL[lastQI] = str(int(J[lastQI]) + 1)
    else:
        larger, smaller = [[JL,CL], [CL,JL]][CBiger]    
        for i in xrange(idx, len(CL)):
            if larger[i] == '?':
                larger[i] = '0'
            if smaller[i] == '?':
                smaller[i] = '9'
    return ''.join(CL), ''.join(JL)
    
fin = open('inputFile.in', 'r')
fout = open('outputFile2.out', 'w')
T = int(fin.readline().strip())

for t in xrange(T):
    line = fin.readline().strip()
    C, J = [arg for arg in line.split(' ')]
    CP, JP = FUN(C, J)
    fout.write('Case #'+str(t+1)+': '+CP+' '+JP+'\n')

fin.close()
fout.close()
