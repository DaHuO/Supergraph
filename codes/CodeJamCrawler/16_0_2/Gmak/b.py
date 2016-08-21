t=int(input())
k=1
while(t>0):
    str=input()
    L=list(str)
    l=len(L)
    count=0
    if(len(L)==1):
        if(L[0]=='-'):
            print("Case #{}: {}".format(k,count+1))
        else:
            print("Case #{}: {}".format(k,count))
    else:
        j=0
        while(l-1>0):
            if(j<len(L) and L[j]!=L[j+1]):
                count+=1
            j+=1
            l-=1
        if(L[len(L)-1]=='-'):
            print("Case #{}: {}".format(k,count+1))
        else:
            print("Case #{}: {}".format(k,count))
    k+=1
    t-=1