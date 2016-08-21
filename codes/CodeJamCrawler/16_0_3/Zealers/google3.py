import math
def b10_n(test,base):
    strtest=str(test)
    strtest=strtest[::-1]
    ijk=0
    xyz=0
    for sd in strtest:
        xyz=xyz+int(sd)*math.pow(base,ijk)
        ijk=ijk+1
    return int(xyz)

def b10_2(num, base):
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

def Prime(numvp):
    zx=int(math.sqrt(numvp))+1
    for dd in range (2,zx):
        if(numvp%dd==0):
            return dd
    return 0



filein=open("C-small-attempt0.in")
fileout=open("C-small-attepmt0.out","w")
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
        test=b10_2(z,2)
        b2=b10_n(test,2)
        b3=b10_n(test,3)
        b4=b10_n(test,4)
        b5=b10_n(test,5)
        b6=b10_n(test,6)
        b7=b10_n(test,7)
        b8=b10_n(test,8)
        b9=b10_n(test,9)
        b10=test
        t10=prime(b10)
        t9=Prime(b9)
        t8=Prime(b8)
        t7=Prime(b7)
        t6=Prime(b6)
        t5=Prime(b5)
        t4=Prime(b4)
        t3=Prime(b3)
        t2=Prime(b2)
        if(t2!=0 and t3!=0 and t4!=0 and t5!=0 and t6!=0 and t7!=0 and t8!=0 and t9!=0 and t10!=0):
            fileout.write(str(test)+" "+str(t2)+" "+str(t3)+" "+str(t4)+" "+str(t5)+" "+str(t6)+" "+str(t7)+" "+str(t8)+" "+str(t9)+" "+str(t10)+"\n")
            count=count+1
        if(count==j):
            break

fileout.close()
filein.close()
        
