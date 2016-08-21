cases = int(input())
answer= ""
for i in range (1,cases+1):
    answer= ""
    number=2
    line=input().split()
    K=int(line[0])
    C=int(line[1])
    S=int(line[2])
    if(K>S):
        answer = "Impossible"
    elif(K == 1):
        answer= "1"
    elif (C==1):
        for l in range (1,K+1):
            number=str(l)
            answer+=number+" "    
    else:
        for j in range (S-1):
            temp=str(number)
            answer+=temp+" "
            number=number+K+1
    print("Case #%i: %s" %(i,answer))