'''
Created on Apr 8, 2016

@author: Thomas
'''
import numpy as np
from math import sqrt
import time

def find_nontrivial_divisor(num):
    #print num    
    
    # Trial Division
    end_ran = int(np.ceil(sqrt(num))) # full range
    end_ran = 1000 # small subset

    max_k = int(np.ceil((end_ran + 1) / 6)) # full range
    
    start = time.time()
    for i in xrange(1, max_k):
        factor = 6*i + 1
        res = num % factor
        if (res == 0):
            return (factor)
        
        factor = 6*i - 1
        res = num % factor
        if (res == 0):
            return (factor)
        
        if (time.time() - start) > 1:
            break

            
    return None

def is_prime(num):
    if find_nontrivial_divisor(num) is None:
        return True
    else:
        return False
    
def convert_to_base(numb, base):
    '''Converts from python binary number to specified Base'''
    num_s = bin(numb)[2:]
    num = 0
    les = len(num_s)
    for i in range(les):
        num = num + (int(num_s[i]) * base**(les-i-1))
    return num

def eval_cand_coin(num):
    ntds = []
    for base in range(2,11):
        numb = convert_to_base(num, base)

        ntd = find_nontrivial_divisor(numb)
        if ntd is None:
            return None
        ntds.append(ntd)
    return ntds

def gen_jamcoins(length, num_jamcoins):
    mid_len = length - 2
    valid_coins = {}

    for i in xrange(2**(mid_len)):
        cand_coin = (2**(length-1) + 1) + (i << 1)
        #print bin(cand_coin)
        res = eval_cand_coin(cand_coin)
        if res is not None:
            valid_coins[cand_coin] = res
        #print len(valid_coins)
        if len(valid_coins) >= num_jamcoins:
            break
            
    return valid_coins
        

if __name__ == '__main__':
    out = {}
    
    with open("input.in", 'rb') as f:
        lines = f.readlines()[1:]
        for idx,line in enumerate(lines):
            line = line.rstrip()
            cols = line.split(" ")
            length = int(cols[0])
            n_jamcoins = int(cols[1])

            out[idx+1] = gen_jamcoins(length, n_jamcoins)


    with open("output.out", 'w') as f:
        f.write("")
        for key, val in out.iteritems():            
            f.write("Case #" + str(key) + ":\n")
            for key,val in val.iteritems():
                s = bin(key)[2:]
                for ntd in val:
                    s = s + " " + str(ntd)
                s = s + '\n'
                f.write(s)