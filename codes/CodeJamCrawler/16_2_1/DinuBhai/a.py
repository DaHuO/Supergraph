t=int(raw_input())
for tt in range(t):
    s=(raw_input())
    s=list(s)
    s.sort()
    ans=[]
    cond=s.count('Z')
    while(cond):
        ans.append(0)
        s.remove('O')
        s.remove('Z')
        s.remove('E')
        s.remove('R')
        cond=cond-1;

    cond=s.count('W')
    while(cond):
        ans.append(2)
        s.remove('T')
        s.remove('W')
        s.remove('O')
        cond-=1
    cond=s.count('U')
    while(cond):
        ans.append(4)
        s.remove('F')
        s.remove('O')
        s.remove('U')
        s.remove('R')
        cond=cond-1
    cond=s.count('X')
    while(cond):
        ans.append(6)
        s.remove('S')
        s.remove('I')
        s.remove('X')
        cond=cond-1
    cond=s.count('G')
    while(cond):
        ans.append(8)
        s.remove('E')
        s.remove('I')
        s.remove('G')
        s.remove('H')
        s.remove('T')
        cond=cond-1
    cond=s.count('O')
    while(cond):
        ans.append(1)
        s.remove('O')
        s.remove('N')
        s.remove('E')
        cond=cond-1
    cond=s.count('R')
    while(cond):
        ans.append(3)
        s.remove('T')
        s.remove('H')
        s.remove('R')
        s.remove('E')
        s.remove('E')
        cond=cond-1
    cond=s.count('F')
    while(cond):
        ans.append(5)
        s.remove('F')
        s.remove('I')
        s.remove('V')
        s.remove('E')
        cond=cond-1

    cond=s.count('S')
    while(cond):
        ans.append(7)
        s.remove('S')
        s.remove('E')
        s.remove('E')
        s.remove('V')
        s.remove('N')
        cond=cond-1
    cond=s.count('I')
    while(cond):
        ans.append(9)
        s.remove('N')
        s.remove('N')
        s.remove('I')
        s.remove('E')
        cond=cond-1
    ans.sort()
    print 'Case #'+str(tt+1)+':',
    print ''.join(str(x) for x in ans)
