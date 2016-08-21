'''
Created on Apr 9, 2016

@author: kingnand
'''
import math

def find_coin(length, num):
    lower_bound = '1' + '0' * (length - 2) + '1' 
    upper_bound = '1' * (length)
    res = []
    for i in range(int(lower_bound, 2), int(upper_bound, 2) + 1):
        arr = isValid(bin(i)[2:])
        if(len(arr) != 9):
            continue
        res.append((bin(i)[2:], ' '.join([str(i) for i in arr])))
        print num
        num-=1
        if num == 0:
            break
    return res


def isValid(jamcoin):
    arr = []
    if not jamcoin.startswith('1') or not jamcoin.endswith('1'):
        return arr
    for i in range(1, 10):
        base = int(jamcoin, i+1)
        if is_prime(base):
            break
        ff = first_factors(base)
        if ff != 1:
            arr.append(ff)
    return arr


def first_factors(n):
    factor = 1  
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i > 2:
                factor = i
                break
    return factor

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
#     for i in range(2, 11):
#         print str(i), factors(int('100011', i))
    with open('C-small-attempt0.txt', 'w') as out:
        with open('C-small-attempt1.in', 'r') as f:
            num=0
            i=0
            for line in f:
                if i==0:
                    num=int(line)
                else:
                    parts = line.split(' ')
                    res = find_coin(int(parts[0].strip()), int(parts[1].strip()))
                    out.write('Case #' + str(i) + ':\n')
                    for (jamcoin, arr) in res:
                        out.write(jamcoin + ' ' + arr)
                        out.write('\n')
                i+=1
    pass
