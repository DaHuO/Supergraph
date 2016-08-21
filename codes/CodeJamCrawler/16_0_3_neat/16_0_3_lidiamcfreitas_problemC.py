
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

from sympy import sieve
from itertools import product

def convertBaseTen(lst, base):
    res = 0
    exp = len(lst)-1
    
    for elem in lst:
        res += elem*base**exp
        exp -=1
    return res

def convertToBinary(number, base):
    string = ""
    rest = number
    
    if(number % base != 1): #first is not a 1
        return False
    
    while(rest != 0):
        binary = rest % base
        if binary != 0 and binary != 1:
            return False    
        
        rest = rest // base
        
        string = str(binary) + string
    return string

def findDivisor(n):
    i = 1 # sieve[1] is 2
    while(i):
        p = sieve[i]
        if(n == p): return False
        if p*p > n: return False
        if n % p == 0: return p
        i += 1
    return False


t = int(input())  # read a line with a single integer


for iteration in range(1, t + 1):
    n, j = [int(x) for x in input().split(" ")]  # read a list of integers, 2 in this case
    permutations = list(product(range(2),repeat=n-2))
    print("Case #{}:".format(iteration))
    
    num = 0
    i = 0
    while(num!=j):
        # print([1] + list(permutations[i]) + [1])
        string = ""
        for base in range(2,11):
            a = findDivisor(convertBaseTen([1] + list(permutations[i]) + [1], base))
            if a == False: 
                string = "error"
                break
            string += str(a) + " "
        if string != "error":
            list_final = [1] + list(permutations[i]) + [1]
            num += 1
            print("".join([str(x) for x in list_final]), string[:-1])  
        i += 1
    



