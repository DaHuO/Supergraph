import sys
def isprime(n):
    n = abs(int(n))
    if n < 2:
        return 0
    if n == 2: 
        return 2  
    if not n & 1: 
        return 2
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return x
    return 0

def interpret(num, base):
    tmp=str(num)[::-1]
    sum=0
    for index,digit in enumerate(tmp):
        if int(digit)==1:
            sum+=base**index
    return sum
    
inputfile=open('coin_input')
input=inputfile.read()
param=input.split('\r\n')
param.remove(param[0])
length=int(param[0].split(' ')[0])
count=int(param[0].split(' ')[1])
print "Case #1:"
for mid in range(0,2**(length-2)):
    answer="1" + (bin(mid)[2:]).zfill(length-2) + "1"
    works=True
    for i in range(2,11):
        num=interpret(answer[:length], i)
        brrr=isprime(num)
        if brrr==0:
           works=False
        else:
            answer+=" %d" % (brrr)
    if works:
        print answer
        count-=1
    if count==0:
        sys.exit()
