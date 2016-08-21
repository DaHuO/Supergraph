# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from multiprocessing import Pool
import numpy as np
import time

#num2div = dict(map(int, line.split(',')) for line in open('/home/avishay/Downloads/cj/coinjam/composites.txt'))

def fisrt_div(n):
    if n % 2 == 0:
        return 2
    for i in range(3, int(n**.5 + 1), 2):
        if n % i == 0:
            return i
    return -1

def is_coinjam(n):
#    print('-=-=-=-n =', n, bin(n)[2:])
    d = fisrt_div(n)
    if d == -1:
        return []
 #   print('d2=%d' % d)
    bin_str = bin(n)[2:]
    #print(bin_str)
    res = [bin_str, d]
    for base in range(3,11):
        d = fisrt_div(int(bin_str, base))
        if d == -1:
            return []
        #print('base=%d,n=%d,d=%d' % (base, int(bin_str, base), d))
        res.append(d)
    return [' '.join(map(str, res))]

def solve(lines):
    N, J = map(int, lines[0].split())
    res = []
    i = 2 ** (N-1) - 1
    z = 0
    pool = Pool()
    queue = []
    while len(res) < J:
        z += 1
        i += 2
        queue.append(pool.apply_async(is_coinjam, (i,)))
        if z > 100000:
            z = 0
            time.sleep(3)
            for r in queue:
                if r.ready():
                    tmp = r.get()
                    if tmp:
                        res.append(tmp[0])
                        if len(res) > J:
                            break
    return res[:J]

lines = open('/home/avishay/Downloads/cj/coinjam/sample').readlines()
num_cases = int(lines[0])
lines_per_case = 1
start = time.time()
o = open('/home/avishay/Downloads/cj/coinjam/small-out', 'w')

for i in range(num_cases):
    res = solve(lines[i*lines_per_case+1:(i+1)*lines_per_case+1])
    print('Case #%d' % (i+1))
    for r in res: print(r)
    o.write('Case #%d:\n' % (i+1))
    for r in res:
        o.write(r + '\n')
    

o.close()
print('runtime=%.2f' % (time.time() - start))