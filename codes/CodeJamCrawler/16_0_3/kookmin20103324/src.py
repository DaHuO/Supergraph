import random
import math

def cradix(n,k):
    v=1
    ans=0
    while n>0:
        ans += (n%10)*v
        n = int(n/10)
        v *= k
    return ans

def isPrime(n):
    if n<2:
        return False
    i=2
    while i*i<=n:
        if(n%i==0):
            return False
        i += 1
    return True
    

file = open("input.txt","r")
output = open("output.txt","w")

testCase = int(file.readline())

n,J = file.readline().split()
n=int(n)
J=int(J)

k = 2**(n-2)
output.write("Case #1:\n")
for y in range(1,k):
    cvt = ("1"+"{0:0"+str(n-2)+"b}").format(y)+"1"
    completed = False
    arr = []
    for z in range(2,11):
        change = cradix(int(cvt),z)
        if isPrime(change) == True:
            break
        else:
            arr.append(change)
        if z == 10:
            completed = True
    if completed == True:
        output.write(cvt+" ")
        for ii in range(0,9):
            kk=2
            while kk*kk<=arr[ii]:
                if(arr[ii] % kk == 0):
                    output.write(str(int(arr[ii]/kk))+" ")
                    break
                kk+=1
        output.write('\n')
        J -= 1
        if(J == 0):
            break
file.close()
output.close()
print("Finish")
