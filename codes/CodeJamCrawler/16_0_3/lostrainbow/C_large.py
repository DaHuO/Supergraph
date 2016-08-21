
def sol(N,J):
    Dividers=['3', '2', '5', '2', '7', '2', '3', '2', '11']
    bin_num='1'+'0'*(N-2)+'1'
    largest=int('1'*N,2)
    ans=bin_num+' '+' '.join(Dividers)+'\n'
    base=int(bin_num,2)
    toAdd=[6,18,30,54,66,78,90,102,114,126,150,198,210,222,246,258,270,282,294,
           306,318,330,354,366,378,390,402,414,438,450,462,474,486,498,510,534,
           582,594,606,630,726,774,786,798,822,834,846,858,870,882,894]
    i=1
    while i<J:
        step=toAdd.pop(0)
        while base+step<largest:
            bin_num=bin(base+step)[2:]
            ans+=bin_num+' '+' '.join(Dividers)
            step+=step
            i+=1
            if i<J:
                ans+='\n'
            else:
                return ans
    return ans



IF=open('C-large.in','r')
OF=open('large_output','w')
CaseN=int(IF.readline())
for i in range(1, CaseN+1):
    pretext='Case #{}:\n'.format(i)
    temp=IF.readline().split()
    N=int(temp[0])
    J=int(temp[1])
    ans=sol(N,J)
    if i<CaseN:
        ans=ans+'\n'
    OF.write(pretext+ans)
    
    
    
IF.close()
OF.close()


            
            