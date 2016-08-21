ls=[]
with open('A-small-attempt1.in','r') as r:
    for lines in r:
        ls.append(lines.strip())
f=open('abcqqq.txt','w')
nums=int(ls[0])
for i in range(nums):
    if ls[i+1]=='0':
        f.write('Case #%d: '%(i+1)+'INSOMNIA'+'\n')
        continue
    j=1
    d={}
    while len(d.keys())!=10:
        m=str(j*int(ls[i+1]))
        for k in m:
            d[k]=1
        j+=1
        print j
    f.write('Case #%d: %d'%(i+1,(j-1)*int(ls[i+1]))+'\n')
    
f.close()