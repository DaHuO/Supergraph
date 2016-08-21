def BT(case,n):
    print("case #{0}: ".format(case),end='')
    if n <= 0:
        print("INSOMNIA")
        return
    temp = 0
    last = 0
    i = 0
    dig = -1
    li_1=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    li_2=[0,1,2,3,4,5,6,7,8,9,]
    while(li_1!=li_2):
        i+=1
        last = n*i
        temp=last
        while(temp!=0):
            dig=temp%10
            temp//=10
            if(li_1[dig]==-1):
                li_1[dig]=dig
                
    print(last)


T=int(input())
li=[]
ct=1
if T>0:
    for i in range(T):
        li.append(int(input()))
    for i in li:
        BT(ct,i)
        ct+=1

