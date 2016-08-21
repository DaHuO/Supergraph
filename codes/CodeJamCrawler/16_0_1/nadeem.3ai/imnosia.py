known=set()
res=[]

def abcd(num1,num2):
    global known
    temp2=num1*num2
    temp1=set(str(temp2))
    temp3=temp1-known
    if len(temp3)!=0:
        res.append(temp2)
        known=known | temp3   
    return temp2

def efgh(num):
    global known
    global res
    known=set()
    res=[]
    for i in range(10000):
        n=abcd(num,i+1)
        if len(known)==10:
            return n


        
N=int(input())
for i in range(N):
    val=int(input())
    if val != 0:
        zz=efgh(val)
        print("Case #{}: {}".format(i+1,zz) )
    else:
        print("Case #{}: INSOMNIA".format(i+1))
