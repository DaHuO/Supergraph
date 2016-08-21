import math
import itertools
import statistics

def readinput():
    inputs=[]
    f=open('input.txt','r')
    for line in f:
        #inputs=line.rstrip().split(' ')
        inputs.append(line.rstrip())
    f.close()
    return inputs
    
def nCr(n,r):
    f=math.factorial()
    return f(n)/(f(r)/f(n-r))
    
#readprimes
file=open('primes.json','r')
primes=file.read()
primes=eval(primes)
file.close()

a=2
coins=[]
factors=[]
lenc=len(coins)
lenp=len(primes)
while lenc<500:
    sa='1'+"{0:030b}".format(a)+'1'
    #print(sa)
    fs=[]
    for i in range(2,11):
        num=int(sa,i) #num in base i
        #print(num)
        #check if prime, has factors
        if(num in primes):
            break
        else:
            factor=-1
            to_check_up_to=math.ceil(math.sqrt(num))+1
            for j in range(lenp): #find factors
                if num%primes[j]==0:
                    factor=primes[j]
                    break
                elif j==to_check_up_to:
                    #if num not in primes:
                        #primes.append(num)
                    break
            if factor!=-1:
                fs.append(factor)
            else:
                break
    if len(fs)==9:
        factors.append(fs)
        coins.append(sa)
        lenc+=1
    a+=1

f=open('output.txt','w')
f.write("Case #1:")
f.write('\n')
lenc=len(coins)
for i in range(lenc):
    f.write(str(coins[i])+' ')
    v=list(map(str,factors[i]))
    f.write(' '.join(v))
    f.write('\n')
    
    

f.close()

"""
inputs=readinput()
cases=int(inputs[0])
inputs=inputs[1:]

f=open('output.txt','w')
for i in range(0,len(inputs)):
    #ints=inputs[i].split(' ')
    #ints=list(map(int,ints))
    solved=solve(inputs[i])
    #solved=list(map(str,solved))
    f.write("Case #{}: ".format(str(i+1))+str(solved))
    f.write('\n')

f.close()
"""