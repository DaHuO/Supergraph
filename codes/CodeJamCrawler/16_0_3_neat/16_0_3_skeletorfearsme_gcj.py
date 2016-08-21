N=16
J=50



def Output(x):
    b=bases2through10(x)
    O=str(b[-1])
    for i in bases2through10(x):
        O = O + " " + str(getFactor(i)) 
    return O

def getFactor(x):
    if x%2==0:
        return 2
    for i in range(3,int(x**0.5)+1,2):
        if x%i==0:
            return i

def isPrime(x):
    if x%2==0:
        return x==2
    for i in range(3,int(x**0.5)+1,2):
        if x%i==0:
            return False
    return not x==1

def bases2through10(decimal):
    a=[]
    for i in range(2,10):
        a+=[TenToBase(decimal,i)]
    return a+[decimal]

def TenToBase(decimal, base):
    n=0
    power=0
    while(decimal>0):
        if decimal%10>0:
            n+=(base**power)
        decimal=decimal//10
        power+=1
    return n

answer=[]
for k in range(2**(N-1)+1,2**N,2):
    i=int(bin(k)[2:])
    if len(answer)==J:
        break
    add=True
    for j in bases2through10(i):
        if isPrime(j):
            add=False
    if add:
        answer+=[i]

# Open a file
fo = open("out.txt", "wb")


fo.write("Case #1:\n")
for a in answer:
    fo.write(Output(a)+"\n")
# Close opend file
fo.close()
