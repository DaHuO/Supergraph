for i in range(int(input())):
    s=str(input())
    s+='+'
    n=len(s)
    #print(s)
    count=0
    for j in range(n-1):
        if(s[j+1]!=s[j]):
            count+=1
    print('Case #',end='')
    print(i+1,end='')
    print(': ',end='')
    print(count)
