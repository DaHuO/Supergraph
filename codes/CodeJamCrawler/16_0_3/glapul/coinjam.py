from tqdm import tqdm
import sys
_ = input()
LEN, J = (int(i) for i in input().split())

def change_base(n, base):
    if base == 2:
        return n
    res = 0
    for i in range(33):
        if (2**i) & n:
            res += base**i
    return res

import sympy
def check_number(n):
    if sympy.ntheory.primetest.isprime(n):
        return (False, -1)
    else:
        return (True, sympy.ntheory.factor_.pollard_rho(n))
    
def check_one(n):
    factors = []
    for base in range(2, 11):
        result, factor = check_number(change_base(n, base))
        if result:
            factors.append(factor)
        else:
            return None

    res = ""
    for i in range(LEN):
        if (2**i) & n:
            res+='1'
        else:
            res+='0'
    return (res[::-1], factors)


print("Case #1:")
from multiprocessing import Pool
pool = Pool(2)
for n in range((2**(LEN - 1))+1, 2**LEN, 22):
    d = pool.apply_async(check_one, (n,))
    try:
        tmp = d.get(timeout = 1)
    except:
        continue
    if tmp != None:
        print(tmp[0], end=" ") 
        for i in tmp[1]:
            print(i, end = " ")
        print("")
        J-=1
        print(J, file=sys.stderr)
        if J == 0:
            break



