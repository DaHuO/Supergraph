def panCakes(filename):
    f=open(filename,'rU')
    tc=int(f.readline())
    g=open('panCakesLarge.out','w')
    for i in range(tc):
        s=f.readline()
        count=0
        last=s.rfind('-')
        if last=='-1':
            g.write(('Case #%d: %d\n')%(i+1,count))
            continue
        while s[last]=='-':
            if s[0]=='+':
                upto=s.find('-')
                if upto!=-1:
                    s='-'*upto+s[upto:]
                    count+=1
                else:
                    break
            if s[0]=='-':
                upto=s.find('+')
                if upto!=-1:
                    s='+'*upto+s[upto:]
                    count+=1
                else:
                    count+=1
                    break
        g.write(('Case #%d: %d\n')%(i+1,count))
panCakes('B-large.in')
