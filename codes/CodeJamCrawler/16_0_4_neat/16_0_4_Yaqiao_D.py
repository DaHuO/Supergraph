from sets import Set
def findPos(set_G,c,K,n):
    Len=K**c
    w=Set([i for i in range(Len)])
    set_L=w.difference(set_G)
    ans=[]
    for i in w:
        if i in set_G:
            ans+=[j for j in range(i*K,i*K+K)]
            
        else:
            ans+=[i*K+n]
    
    return Set(ans)

if __name__=="__main__":
    ls=[]
    with open('D-small-attempt1.in','r') as r:
        for lines in r:
            ls.append(lines.strip())
    f=open('new_result13.txt','w')
    nums=int(ls[0])
    for test in range(nums):
        K,c,S=ls[test+1].split()
        K=int(K)
        c=int(c)
        S=int(S)
        """
        whole_set=[]
        for i in range(K):# initial pos of G
            set_G=Set([i])
            for j in range(2,c+1): # complexity
                set_G=findPos(set_G,j-1,K,i)
            whole_set.append(set_G)
        """
        ans=[str(t+1) for t in range(S)]
        
        #for t in range(S):
            #ans.append(str(whole_set[t].pop()+1))
        final=" ".join(Set(ans))    
        f.write('Case #%d: %s'%(test+1,final)+'\n')
    f.close()
