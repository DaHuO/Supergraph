f = open('A-large.in','r')
g = open('A-large.out','a+')
cases = int(f.readline())
for x in range(cases):
    c = [0,0,0,0,0,0,0,0,0,0]
    a = int(f.readline())
    q = a
    if a==0:
        pr = 'Case #'+ str(x+1)+': INSOMNIA'
        print pr
        g.writelines(pr)
        g.writelines('\n')
    else:
        d=1
        while 1:
            b = list(str(a))
            for y in b:
                c[int(y)] = 1
            
            if 0 not in c:
                pr = 'Case #'+ str(x+1)+': '+str(a)        
                print pr
                g.writelines(pr)
                g.writelines('\n')
                break
            a=q*(d+1)
            d+=1

f.close()
g.close()
