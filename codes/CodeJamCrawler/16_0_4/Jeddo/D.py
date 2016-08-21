def check(K,C,S):
    needed = max(K-C+1,1)
    if S<needed:
        return 'IMPOSSIBLE'
    #for C =1
    pat =0
    char = 1
    st = pat + char
    for i in range(2,C+1):
        pat = (st-1)*K
        char += 1
        if char>K:
            char = K
        st = pat + char
    res = range(st,st + needed)
    return ' '.join(map(str,res))

if __name__=='__main__':
    inF = open('D-small-attempt2.in','r')
    out = open('D-small.out','w')
    T = int(inF.readline())
    for case in range(1,T+1):
        K,C,S = map(int,inF.readline().split(' '))
        out.write('Case #'+str(case)+': '+check(K,C,S)+'\n')
    out.close()
    
