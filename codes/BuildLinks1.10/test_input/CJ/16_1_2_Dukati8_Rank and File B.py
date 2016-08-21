T=int(input())
for i in range (T):
    N=int(input())
    myheights=[]
    for j in range (2*N-1):
        line=input().split()
        for k in range (N):
            line[k]=int(line[k])
        myheights.append(line)
    heightcount={}
    for j in range (2501):
        heightcount[j]=0
    for row in myheights:
        for height in row:
            heightcount[height]+=1
    output=""
    for j in range (2501):
        if heightcount[j]%2==1:
            output+=" " + str(j) 
    print ("Case #" + str(i+1) + ":" + output)
