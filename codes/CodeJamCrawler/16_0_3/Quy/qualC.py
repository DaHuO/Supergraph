__author__ = "Quy Doan"

import math
import sys

output_file = sys.argv[1]

pl = []

with open("prime_list","r") as reader:
    pl = map(long,reader.readline().split())

PL_LEN = len(pl)


def toBase(n,base):
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res = str(n % base) + res
        n /= base
    return res

def baseTo(n_str,base):
    res = 0
    pw = 1L
    for digit in n_str[::-1]:
        res += long(digit) * pw
        pw *= base
    return res

def isPrime(n):
    if n < 2:
        return 0    
    lim = long(math.sqrt(n)+1)
    i = 1
    while i < PL_LEN and pl[i] <= lim:
        if n % pl[i] == 0:
            return pl[i]
        i += 1
    return 0


fr = baseTo("10000000000000000000000000000001",2)
to = baseTo("11111111111111111111111111111111",2)

base = [2,3,4,5,6,7,8,9,10]

while True:
    if fr % 3L == 0:
        break
    else:
        fr += 2
print fr,to

with open(output_file,"w") as writer:
    writer.write("Case #1:\n")
    count = 0
    i = fr
    while True:
        arr = [0 for x in range(11)]
        nb = [0L for x in range(11)]
        coin = toBase(i,2)
        print coin
        isCoin = True
        for b in base:
            nb[b] = baseTo(coin,b)
            arr[b] = isPrime(baseTo(coin,b))
            if arr[b] == 0:
                isCoin = False
        if isCoin:
            count += 1
            print "Counter = ",count
            writer.write(" ".join(map(str,[coin,arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9],arr[10]]))+"\n")
            print coin
            print nb[2],nb[3],nb[4],nb[5],nb[6],nb[7],nb[8],nb[9],nb[10]
            print arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9],arr[10] 
        if count == 500:
            break
        i += 6

     


