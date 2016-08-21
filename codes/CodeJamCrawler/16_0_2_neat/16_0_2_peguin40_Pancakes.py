t = int(input())
for k in range(1,t+1):
    n=str(input())
    flipped = True
    times=0
    n=list(n)
    while flipped:
        bottom=-1
        for i in range(1,len(n)+1):
            if n[-i]=='-':
                bottom=len(n)-i
                break
        if bottom==-1:
            print("Case #"+str(k)+": 0")
            flipped=False
        else:
            times+=1
            for j in range(0,bottom+1):
                if n[j]=='-':
                    n[j]='+'
                else:
                    n[j]='-'
            count=0
            for item in n:
                if item=='-':
                    count+=1
            if count==0:
                print("Case #"+str(k)+": "+str(times))
                flipped=False
