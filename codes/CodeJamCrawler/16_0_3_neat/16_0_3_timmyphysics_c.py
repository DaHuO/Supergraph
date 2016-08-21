import sys
from operator import itemgetter
import math

def changeBase(num, base):
    newnum = 0
    power = len(num)-1
    #print num
    for i in num:
        newnum+= int(i)*(base**power)
        #print newnum
        power-=1
    #print newnum
    return newnum

def isPrime(num):
    #print type(num)
    if num%2 == 0:
        return 2

    # loop up to sqrt(n)
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return i
    return -1 # or False
'''
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(num):
    lc = num, 
    return lowestcd
'''
def validate(J_str):
    # change base, check if prime    
    bases = [2,3,4,5,6,7,8,9,10]
    base_factors = []
    
    
    for b in bases:
        newnum = changeBase(J_str, b)
        #print newnum
        check = isPrime(newnum)
        #print check
        if check == -1:
            return False,[]
        else:
            base_factors.append(check)
            
    return True,base_factors
    


def calculate(N, J):
    # length is N, need J jamcoins with length N

    # there are (N-2)^2 different numbers to consider...
    J_str = '1'
    for n in range(N):
        J_str+='0'
    J_str+='1'
    J_found = []
    J_count = 0
    
    for i in range(0,(N-2)**2):
        binnm = str(bin(i))[2:]
        #pad it if it is too short!
        J_str = '1'
        for jj in range(0, (N-2)-len(binnm)):
            J_str += '0'
        J_str += binnm+'1'
        #print J_str
        valid, factors = validate(J_str)
        if not valid:
            continue
        J_count += 1
        #print J_count
        J_found.append([J_str,factors])
        if J_count >= J:
            return J_found
            
    
            
    return J_found # didn't find a possible option

infile = open(sys.argv[1],'r')

numcases = int(infile.readline().strip())
outfile = open(sys.argv[1].replace('.in','.out'),'w')
for n in range(numcases):
    #N = int(infile.readline().strip())
    c_i_str = infile.readline().strip().split()
    N = int(c_i_str[0])
    J = int(c_i_str[1])
    #print 'getting difference'
    diff = calculate(N, J)
    print diff
    ans = ''
    outfile.write("Case #" + str(n+1)+":\n")# + ans + '\n')
    for j in diff:
        outfile.write(j[0])
        ans = j[0]
        for k in j[1]:
            outfile.write(" " + str(k))
            ans += ' ' + str(k)
        outfile.write("\n")
        print ans

outfile.close()
