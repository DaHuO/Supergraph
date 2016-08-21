import sys
def al(d):
    for k in d:
        if d[k]==0:
            return False
    return True
inp=open('input.txt','r')
out=open('output.txt','w')
t=int(inp.readline())   
for ti in range(t):
    i=int(inp.readline())
    out.write('Case #'+str(ti+1)+': ')
    if i== 0:
        out.write('INSOMNIA\n')
    else :
        d={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        n=i
        while(not al(d)):
            ns=str(n)
            for ch in ns:
                d[int(ch)]=1
            n=n+i
        out.write(str(n-i)+'\n')
inp.close()
out.close()
    
    
