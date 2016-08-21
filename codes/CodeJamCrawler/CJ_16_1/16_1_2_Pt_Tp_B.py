# -*- coding: utf-8 -*-


def search(ii):
    global N,R,C,L,nC,nR,isSkipC,isSkipR
    if ii >= len(L):
        return True    
    l = L[ii]

    isC = nC < N
    if isC:
        for i in range(nR):
            if R[i] != -1 and R[i][nC] != l[i]:
#                print 'ii,i,nc=',ii,i,nC
#                print l
#                print '---'
#                for j in range(nR):
#                    print R[j]
#                print '---'
                isC = False
                break

    if isC and (nC > 0) :
        if C[nC-1] == -1:
            j = 2
        else:
            j = 1
        if nC -j >= 0:
            for i in range(N):
                if C[nC-j][i] >= l[i]:
                    isC = False
                    break

    if isC:
#        print '-'*ii,ii,'-->C'
        C[nC] = l
        nC += 1
        if (search(ii+1)):
            return True
        nC -= 1
        C[nC] = -1
        isC = False
    isR = (nR < N)
    if isR:
        for i in range(nC):
            if C[i] != -1 and C[i][nR] != l[i]:
                isR = False
                break

    if isR and (nR > 0) :
        if R[nR-1] == -1:
            j = 2
        else:
            j = 1
        if nR -j >= 0:
            for i in range(N):
                if R[nR-j][i] >= l[i]:
                    isR = False
                    break

    if isR:
#        print '-'*ii,ii,'-->R'
        R[nR] = l
        nR += 1
        if (search(ii+1)):
            return True
        nR -= 1
        R[nR] = -1
        isR = False
    
    if not (isSkipC or isSkipR):
        if nC < N:
            isSkipC = True
            nC += 1
            if search(ii):
                return True
            nC -= 1
            isSkipC = False
        if nR < N:
            isSkipR = True
            nR += 1
            if search(ii):
                return True
            nR -= 1
            isSkipR = False
    return False
                
    



f = open('C:\\Users\\Ton\\Desktop\ggcj\\Round1A2016\\B\\B-small-attempt1.in')
fo= open('C:\\Users\\Ton\\Desktop\ggcj\\Round1A2016\\B\\B-small-attempt1.out','wb')
T = int(f.readline())

for tt in range(1,T+1):
    N = int(f.readline())
    L = []
    for i in range(N+N-1):
        L.append(map(int,f.readline().split()))
    L.sort()
    R = [-1]*N
    C = [-1]*N
    R[0] = L[0]
    nR = 1
    nC = 0
    isSkipC = False
    isSkipR = False
    a = search(1)
    ans = []
    for i in range(1,N):
        if R[i] == -1:
            ans = [C[j][i] for j in range(N)]
            break
    if ans == []:
        for i in range(N):
            if C[i] == -1:
                ans = [R[j][i] for j in range(N)]
                break
    s = 'Case #{0}:'.format(tt)
    for a in ans:
        s += ' '+str(a)
    print s
    fo.write(s+'\n')
f.close()
fo.close()