t=int(raw_input())
for z in range(t):
    c=raw_input()
    j=0
    if c.count('-')==len(c):
        print 'Case #%i:'%(z+1),1
    elif not '-' in c:
        print 'Case #%i:'%(z+1),0
    else:
        while '-' in c:
            x=c[0]
            for i in range(len(c)):
                if x==c[i]:
                    if x=='+':
                        c=c[:i]+'-'+c[i+1:]
                    else:
                        c=c[:i]+'+'+c[i+1:]
                else:
                    break
            j+=1
        print 'Case #%i:'%(z+1),j
