import math
def base10to2(num, base):
    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base error")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return int(converted_string)

def checkPrime(numvp):
    zx=int(math.sqrt(numvp))+1
    for dd in range (2,zx):
        if(numvp%dd==0):
            return dd
    return 0

def base10toN(test,base):
    strtest=str(test)
    strtest=strtest[::-1]
    ijk=0
    xyz=0
    for sd in strtest:
        xyz=xyz+int(sd)*math.pow(base,ijk)
        ijk=ijk+1
    return int(xyz)

filein=open("C-small-attempt1.in")
fileout=open("C-small-attepmt1.out","w")
asdf=[]
for get in filein:
    asdf.append(get.rstrip('\n'))
times=int(asdf[0])
for x in range(1,times+1):
    count=0
    xyz=asdf[x]
    xyz=xyz.split(" ")
    n=int(xyz[0])
    j=int(xyz[1])
    last=int(math.pow(2,n)-1)
    first=int(math.pow(2,n-1)+1)
    fileout.write("Case #"+str(x)+":\n")
    for z in range(first,last+1,2):
        test=base10to2(z,2)
        base2=base10toN(test,2)
        base3=base10toN(test,3)
        base4=base10toN(test,4)
        base5=base10toN(test,5)
        base6=base10toN(test,6)
        base7=base10toN(test,7)
        base8=base10toN(test,8)
        base9=base10toN(test,9)
        base10=test
        divisor2=checkPrime(base2)
        divisor3=checkPrime(base3)
        divisor4=checkPrime(base4)
        divisor5=checkPrime(base5)
        divisor6=checkPrime(base6)
        divisor7=checkPrime(base7)
        divisor8=checkPrime(base8)
        divisor9=checkPrime(base9)
        divisor10=checkPrime(base10)
        if(divisor2!=0 and divisor3!=0 and divisor4!=0 and divisor5!=0 and divisor6!=0 and divisor7!=0 and divisor8!=0 and divisor9!=0 and divisor10!=0):
            fileout.write(str(test)+" "+str(divisor2)+" "+str(divisor3)+" "+str(divisor4)+" "+str(divisor5)+" "+str(divisor6)+" "+str(divisor7)+" "+str(divisor8)+" "+str(divisor9)+" "+str(divisor10)+"\n")
            count=count+1
        if(count==j):
            break

fileout.close()
filein.close()
        
