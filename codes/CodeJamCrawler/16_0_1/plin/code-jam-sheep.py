a=open('sheep-in-large.txt','r')
b=a.readlines()
for i in range(len(b)):
    b[i]=b[i].rstrip('\n')
a.close()

c=open('sheep-out-large.txt','w')

for j in range(1,len(b)):
    noSleep=False
    result="Case #"+str(j)+": "
    checked=[]
    tempMult=1
    x=b[j]
    x=int(x)
    num=tempMult*x
    while len(checked)!=10:
        digits=list(str(num))
        for digit in digits:
            if digit not in checked:
        	    checked.append(digit)
        tempNum=tempMult*x
        tempMult+=1
        num=tempMult*x
        if (tempNum==num):
            result+="INSOMNIA"
            noSleep=True
            break
    if not noSleep:
        result+=str((tempMult-1)*x)
    c.write(result+"\n")
c.close()