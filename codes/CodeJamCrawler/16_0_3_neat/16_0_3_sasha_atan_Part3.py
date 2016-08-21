
def isPrime(n):
    if n<2:
        return [True, 0]
    if n == 2:
        return [True, 0]
    if not n & 1:
        return [False, 2]
    for x in range(3,int(n**0.5)+1,2):
        if n%x == 0:
            return [False, x]
            
    return [True, 0]
    

def findFactor(n):
    i=2
    if i%2==0:
        return 2
    for x in range(2, int(n**0.5)+2,2):
        if n%x == 0:
            return x
    return "EXCEPTION"
    

print "Case #1:"
L = []        

numTests = int(raw_input())

for line in range(1, numTests+1):
    q, p = [s for s in raw_input().split(" ")]
    q=int(q); p=int(p)


for i in range(1,2**(q-1) ,2):
    binaryNum = bin(2**(q-1) + i)[2:]
    primality = False;
    factors = []
    for j in range(2,11):
        n = int(binaryNum,j)
        a, b = isPrime(n)
        if a:
            primality = True
            break;
        else:
            factors.append(b)
            
    if not primality:
        L.append(binaryNum)
        print binaryNum, (str(factors)[1:-1]).replace(',','')
    if len(L)>= p:
        break    