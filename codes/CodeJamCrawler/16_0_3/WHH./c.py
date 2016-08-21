import math
import time

def checknotprime(n):
    a = time.time()
    if n<2 or n%2==0:
        return 0
    for i in range(3, int(math.sqrt(n))+1, 2):
        if time.time()-a >0.00001:
            return 0
        if n%i == 0:
            return i
    return 0

def number(binary, base):
    number = 0
    count = len(binary)
    for i in range(len(binary)):
        count-=1
        number += int(binary[i])*(base**count)
    return number

x = time.time()

    
infile = open("C-large.in", "r")
outfile = open("C-large.out", "w")
print("Case #1:", file=outfile)
t = infile.readline()
n, j = infile.readline().split()
n = int(n)
j = int(j)

count = 0
decimal = 2**(n-1)+1
binary = bin(decimal)[2:]
while count < j and len(binary)==n:
    nontrivial = []
    binary = bin(decimal)[2:]
    
    if binary[len(binary)-1] != '1':
        
        decimal+=1
        continue
    for base in range(2, 11):
        num = number(binary, base)
        
        a = checknotprime(num)
        if not a:
            break
        if a:
            nontrivial.append(a)
    if a:
        print(count)
        print("{}".format(binary), end=' ', file=outfile)
        for i in range(9):
              print("{}".format(nontrivial[i]), end=' ', file=outfile) 
        print('', file=outfile)
        count+=1
    decimal+=1

print("done")
print(time.time() -x)
infile.close()
outfile.close()
