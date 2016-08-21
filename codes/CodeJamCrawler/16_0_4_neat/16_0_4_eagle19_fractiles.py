t=int(input())
counter=1

while(counter<=t):
    k,c,s=map(int,input().split())
    print("Case #{}:".format(counter),end=' ')
    for i in range(1,k+1):
        print(i,end=' ')
    print()    
    counter+=1    
