def isPrime(num):
    if num<2:
        return (False,0)
    elif num==2:
        return (False,0)
    else:
        sqrt=int(num**(1/2))+2
        for i in range(2,sqrt):
            if num%i==0: return (False,i)
    return (True,0)
def convertToBase(i,base):
    digits=list(i)
    mul=1
    ans=0
    while digits:
        d=digits.pop()
        ans+=int(d)*mul
        mul=mul*base
    return ans

combos=[bin(x)[2:] for x in range(32769,65536,2)]

ans=[]
ans_divisor=[]
count=0
for i in combos:
    divisior=[]
    for base in range(2,11):
        k=convertToBase(i,base)
        p,d=isPrime(k)
        if p: break
        else: divisior.append(d)
    if len(divisior)==9:
        count+=1
        ans.append(i)
        ans_divisor.append(divisior)
    if count==50: break


print("Case #1:")
for i in range(0,len(ans)):
	print(ans[i],end=" ")
	for j in ans_divisor[i]: print(j,end=" ")
	print()

#print(len(ans))

