def lastWord(filename):
    f=open(filename,'rU')
    tc=int(f.readline())
    g=open('lastsmall.out','w')

    for test in range(tc):
        line=f.readline()
        x=line[0]
        s=line[0]
        for i in line[1:]:
            if i<s[0]:
                s+=i
            else:
                s=i+s
        g.write(('Case #%d: %s\n')%(test+1,s))
    f.close()
    g.close()
lastWord('A-large (1).in')
