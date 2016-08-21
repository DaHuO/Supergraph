import math
def toBase(num, base):
    power = len(str(num))-1
    output = 0
    for i in range (len(str(num))):
        output+= base**power * int(str(num)[i])
        power = power-1
    
    return output

def findDivisor(num):
    if num % 2 == 0:
        return 2
    tries = 0
    for i in range(3,math.ceil(math.sqrt(num))+1,2):
        tries = tries+1
        if tries > 1000000:
            break
        if num % i == 0:
            return i
    return 0

def BintoDec(num):
    decOut = 0
    power = 0
    while not num == 0:
        decOut = decOut + 2**power * (num % 10)
        num = num//10
        power = power+1
    return decOut
def DecToBin(num):
    out = 0
    power = 0
    while not num==0:
        out+=(10**power) *(num%2)
        num//=2
        power = power+1
    return out

def incrementBinary(num):
    temp = BintoDec(num)
    temp = temp + 2
    num = DecToBin(temp)
    return num

t = int(input())
for i in range(t):
    length = int(input())-1
    jamNum = int(input())
    print("Case #"+str(i+1)+":\n")
    num = 1
    
    for j in range(length):
        num = num*10
    num = num + 1

    for j in range(jamNum):
        divisors = [0,0,0,0,0,0,0,0,0 ]
        while True:
            for k in range (2,11):
                
                divisors[k-2] = findDivisor(toBase(num,k))
                if divisors[k-2] == 0:
                    num = incrementBinary(num)
                    break
            if not divisors[8]==0:
                break
            
        print(str(num))
        for k in range(0,9):
            
            print(str(" "+ str(divisors[k])))
        
        num = incrementBinary(num)
        
        

        
