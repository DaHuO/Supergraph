t=eval(input())

for i in range(t):
    inp=(input())
    inp=inp.split(" ")
    k=int(inp[0])
    c=int(inp[1])
    s=int(inp[2])


    if(k==1):
        print("Case #",i+1,": 1",sep="")

    elif(c==1):
        if(s<k):
            print("Case #",i+1,": IMPOSSIBLE",sep="")
        else:
            print("Case #",i+1,":",sep="",end="")
            for j in range(k):
                print(" ",j+1,sep="",end="")
            print()
    else:
        if(s<(k-1)):
            print("Case #",i+1,": IMPOSSIBLE",sep="")
        else:
            print("Case #",i+1,":",sep="",end="")
            for j in range(1,k):
                print(" ",j+1,sep="",end="")
            print()
        
