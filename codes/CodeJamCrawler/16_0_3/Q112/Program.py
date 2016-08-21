import sys
import os
from itertools import *

Out = open(os.path.dirname(os.path.abspath(__file__))+'/'+sys.argv[2],'w')
if sys.argv[1] == 'Test':
    N, J = 6,3
elif sys.argv[1] == 'Small':
    N, J = 16, 50
elif sys.argv[1] =='Large':
    N, J = 32, 500
else:
    print('Please enter one of the three options Test, Small or Large')
    __name__==''
    
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
   
def isprime(n):
    for m in range(2, int(n**0.5)+1):
        if not n%m:
            return m
    return True
            
if __name__ == '__main__':
    Out.write('Case #1: \n')
    count = 0
    S = powerset([i for i in range(1,N-1)])
    for s in S:
        print(s)
        s = list(s)
        if len(s)%2 != 0:
            continue
        if not sum([(-1)**x for x in s]) == 0:
            continue
        M = 10**(N-1)+1
        for i in range(1,N-1):
            if i in s:
                M += 10**(N-1-i)         
        Out.write('{} {} {} {} {} {} {} {} {} {} \n'.format(M, 3, 2, 5, 2, 7, 2, 3, 2, 11))
        #Numbers with the properties of M automatically produce jam coins with the above prime divisors.
        count += 1
        if count == J:
            break
                

                    
                  
            
