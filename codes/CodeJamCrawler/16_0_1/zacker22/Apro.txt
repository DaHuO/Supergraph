L=[]
for j in range(int(input())):
    L.append(input())
for j in range(len(L)):
    s=L[j]
    l=s[0]
    for i in range(1,len(s)):
        if ord(s[i])>=ord(l[0]):
            l=s[i]+l[:]
        else:
            l=l[:]+s[i]
            
    print("Case #{}: {}".format(j+1,l))  