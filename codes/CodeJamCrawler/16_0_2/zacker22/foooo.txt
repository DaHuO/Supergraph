n=int(input())
S=[]
for i in range(n):
    S.append(input())
j=0
for s in S:
        a=s[::-1]
        m=['-','+']
        c=0
        for i in a:
            if i==m[c%2]:
                c+=1
        print("Case #{}: {}".format(j+1,c))
        j+=1