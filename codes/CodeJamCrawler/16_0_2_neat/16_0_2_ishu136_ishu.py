t=int(input())
for _ in range(t):
    n=input()
    li=list(n)
    length=len(li)
    i=0
    j=length
    count=0
    if(length==1):
        if(li[i]=='-'):
            print('Case #{}: {}'.format(_+1,count+1))
        else:
            print('Case #{}: {}'.format(_+1,count))
    else:
        while(length-1>0):
            if(i<len(li) and li[i]!=li[i+1]):
                count+=1
            length-=1
            i+=1
        if(li[j-1]=="-"):
            print('Case #{}: {}'.format(_+1,count+1))
        else:
            print('Case #{}: {}'.format(_+1,count))