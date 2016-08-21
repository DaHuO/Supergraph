t=int(raw_input())
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(0,t):
    n=int(raw_input())
    ans="Case #"+str(i+1)+":" 
    arr=map(int,raw_input().split(' '))
    arr2=arr[:]
    while (sum(arr)>2):  
        a=arr.index(max(arr))
        ans+=" "+alpha[a]
        arr[a]=arr[a]-1
        if 2*max(arr)>sum(arr):
            a=arr.index(max(arr))
            ans+=alpha[a]
            arr[a]=arr[a]-1
    a=arr.index(max(arr))
    ans+=" "+alpha[a]
    arr[a]=arr[a]-1
    a=arr.index(max(arr))
    ans+=alpha[a]
    print ans
        