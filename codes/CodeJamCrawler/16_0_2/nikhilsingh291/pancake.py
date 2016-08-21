n=int(raw_input())
for f in range(0,n):
    dat=raw_input()
    st=list(dat)
    l=len(st)
    count=0


    for i in range(0,l):
        if (st[0]!=st[i]):
            for j in range(0,i+1):
                st[j]=st[i]
            count=count+1
                
        
        
        
    if (st[0]=='+'):
        print'Case #%s: %s'%(f+1,count)
    else:
        print'Case #%s: %s'%(f+1,count+1)
  
    
