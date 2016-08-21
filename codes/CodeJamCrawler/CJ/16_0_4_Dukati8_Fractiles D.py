T=int(input())
for i in range (T):
    line1=input().split()
    K=int(line1[0])
    ans="1"
    for j in range (K-1):
        ans+=" "
        ans+= str(j+2)
    print ("Case #" + str(i+1) + ": " + ans)
