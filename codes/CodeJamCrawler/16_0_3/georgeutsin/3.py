import math

def dec_to_bin(x):
    return int(bin(x)[2:])
    
def binToNum(binstr, base):
    num = 0
    for i in range(len(binstr)):
        num+=int(binstr[len(binstr)-1-i])* base**i
    return num
        
def isNotPrime(num):
    a=2
    while math.sqrt(num)+1 > a :
        if num%a==0 & a!=num:
            return a
            break
        a += 1
    else: # loop not exited via break
        return False

t = input()
line = raw_input().split()
n = int(line[0])-3
j = int(line[1])

minNum = 0
maxNum = 2**(n+1)

count = 0
print "Case #1:"
for i in range(minNum, maxNum):
    binstr = "1" + str(dec_to_bin(i)).zfill(n+1)+ "1"
    val = []
    for a in range(2,11):
        x = isNotPrime(binToNum(binstr, a))
        if not x:
            break
        else:
            val.append(x)
            
    if(len(val) == 9):
        print binstr + " " + str(val[0]) + " " + str(val[1]) + " " + str(val[2]) + " " + str(val[3]) + " " + str(val[4]) + " " + str(val[5]) + " " + str(val[6]) + " " + str(val[7]) + " " + str(val[8])
        count += 1
        
    if count >50:
        break
   
