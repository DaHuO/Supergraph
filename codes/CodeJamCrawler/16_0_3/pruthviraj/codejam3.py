import itertools,random
from itertools import count,islice
from math import sqrt
binseq = []
def gen_samp_coin(length):
    ran = random.choice(binseq)
    binseq.remove(ran)
    return ran

def is_prime(n):
    nums = [int(n,2),int(n,3),int(n,4),int(n,5),int(n,6),int(n,7),int(n,8),int(n,9),int(n,10)]
    for each in nums:
        if each > 1 and all(each%i for i in islice(count(2), int(sqrt(each)-1))):
            return True
    return False

def get_factor(n):
    for each in range(2,int(n**0.5)+1):
        if n % each == 0:
            return each

def gen_factors(n):
    facts = []
    for base in range(2,11):
        num_in_base = int(n,base)
        facts.append(get_factor(num_in_base))
    return facts

def gen_jam_coin(length,J):
    global binseq
    binseq = ["".join(seq) for seq in itertools.product("01", repeat=length)]
    binseq = [x for x in binseq if x[0] == '1' and x[-1] == '1']
    f = []
    generated = 0
    while generated != J:
        samp = gen_samp_coin(length)
        if not is_prime(samp):
            facts = gen_factors(samp)
            f.append([samp]+facts)
            generated += 1
    return f

no_of_test = int(input())

for each in range(0,no_of_test):
    l = raw_input().split()
    N = int(l[0])
    J = int(l[1])
    facts = gen_jam_coin(N,J)
    print("Case #"+ str(each+1) + ":")
    for coin in facts:
        print(' '.join([str(x) for x in coin]))

