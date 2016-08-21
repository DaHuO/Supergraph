#arr=["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
t=int(raw_input())
for j in range(0,t):
    s=raw_input()
    arr=[]
    num=[]
    count=[0,0,0,0,0,0,0,0,0,0]
    n=len(s)
    for i in s:
        arr.append(i)
    s=arr
    for p in range(0,n):
        if(s[p]=='Z'):
            s[p]=-1
            for q in range(0,n):
                if(s[q]=='E'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='R'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='O'):
                    s[q]=-1
                    break
            count[0]+=1
    for p in range(0,n):
        if(s[p]=='W'):
            s[p]=-1
            for q in range(0,n):
                if(s[q]=='T'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='O'):
                    s[q]=-1
                    break
            count[2]+=1
    for p in range(0,n):
        if(s[p]=='G'):
            s[p]=-1
            for q in range(0,n):
                if(s[q]=='E'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='I'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='H'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='T'):
                    s[q]=-1
                    break
            count[8]+=1
    for p in range(0,n):
        if(s[p]=='T'):
            s[p]=-1
            for q in range(0,n):
                if(s[q]=='H'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='R'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='E'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='E'):
                    s[q]=-1
                    break
            count[3]+=1
    for p in range(0,n):
        if(s[p]=='R'):
            s[p]=-1
            for q in range(0,n):
                if(s[q]=='F'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='O'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='U'):
                    s[q]=-1
                    break
            count[4]+=1
    for p in range(0,n):
        if(s[p]=='F'):
            s[p]=-1
            for q in range(0,n):
                if(s[q]=='I'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='V'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='E'):
                    s[q]=-1
                    break
            count[5]+=1
    for p in range(0,n):
        if(s[p]=='X'):
            s[p]=-1
            for q in range(0,n):
                if(s[q]=='S'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='I'):
                    s[q]=-1
                    break
            count[6]+=1
    for p in range(0,n):
        if(s[p]=='S'):
            s[p]=-1
            for q in range(0,n):
                if(s[q]=='E'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='V'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='E'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='N'):
                    s[q]=-1
                    break
            count[7]+=1
    for p in range(0,n):
        if(s[p]=='O'):
            s[p]=-1
            for q in range(0,n):
                if(s[q]=='E'):
                    s[q]=-1
                    break
            for q in range(0,n):
                if(s[q]=='N'):
                    s[q]=-1
                    break
            count[1]+=1
    for p in range(0,n):
        if(s[p]=='I'):
            count[9]+=1
    x1=""
    for i in range(0,10):
        while(count[i]>0):
            x1=x1+str(i)
            count[i]-=1
    print "Case #"+str(j+1)+": "+x1
    
            
            
            
                
            
        
        
        
    
        
    
