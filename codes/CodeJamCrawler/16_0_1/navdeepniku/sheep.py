def sleep(n):
    if n==0:
        
        return 'INSOMNIA'
    table=set()
    tab=set(['1','2','3','4','5','6','7','8','9','0'])
    k=1
    t=n
    while True:
        table.update(list(str(t)))
        if table==tab:
            
            return t
        k=k+1
        t=k*n


f = open('A-large.in')
fo = open('output.out','wb')
t= int(f.readline().strip())
for i in range(1,t+1):
    n= int(f.readline().strip())
    r=sleep(n)
    fo.write('Case #'+str(i)+': '+str(r)+'\n')

fo.close()
