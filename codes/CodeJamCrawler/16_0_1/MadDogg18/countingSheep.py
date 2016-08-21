#Counting Sheep

def countingSheep(N,i=1,digits=set()):
    if type(N)!=int:N=int(N)
    if len(digits)==10:
        return N*(i-1)
    elif i==100:
        a="INSOMNIA"
        return a
    else:
        for digit in listDigits(N*i):
            if str(digit) not in digits:
                digits.add(str(digit))
        return countingSheep(N,i+1,digits)

def listDigits(n):
    listDigits=[]
    while n>0:
        d=n%10
        listDigits.append(d)
        n=n//10
    return listDigits

t = int(input())
for i in range(1, t + 1):
  print("Case #%d: %s" %(i,countingSheep(input(),1,set())))

