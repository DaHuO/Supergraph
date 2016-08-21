t = int(input())
complete_set=[1,2,3,4,5,6,7,8,9,0]
for i in range(t):
    z=1
    n=input()
    seen_set=[]
    if(int(n)==0):
            print('case #',i+1,':',' INSOMNIA',sep='')
            continue
    while(set(seen_set)!=set(complete_set)):
        p=str(int(n)*z)
        z=z+1
        for w in p:
            seen_set.append(int(w))
    print('case #',i+1,':',' ',p,sep='')
    seen_set=[]
    
        
        
