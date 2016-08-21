fin=open('A-large.in', 'r')
fout=open('out_small.out', 'w')
t=int(fin.readline())
a=set(['1','2','3','4','5','6','7','8','9','0'])
for x in range(t):
    n=int(fin.readline())
    if n==0:
        fout.write('Case #%d: '%(x+1))
        fout.write('INSOMNIA'+'\n')
        continue
    s=set([])
    i=1
    while s!=a:
        s=s.union(set(list(str(i*n))))
        i+=1
    fout.write('Case #%d: '%(x+1))
    fout.write(str((i-1)*n)+'\n')
fin.close()
fout.close()
    
    
