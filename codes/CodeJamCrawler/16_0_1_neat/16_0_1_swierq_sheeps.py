#!/usr/bin/env python


file='large.in'

def digits(n):
    return set((int(x) for x in str(n)))

def count_sheps(n, ref, our=None, i=1):
    if our is None:
        our = set()
    if n==0:
        return "INSOMNIA"

    our.update(digits(n*i))

    if our==ref:
        return n*i
    else:
        return count_sheps(n, ref, our, i+1)

def output(n,result):
    print("Case #{}: {}".format(n,result))



ref = set(range(10))
with open(file,'r') as f:
    N = int(f.readline())
    i=0
    while True:
        i+=1
        try:
            x = int(f.readline())
        except:
            break;
        output(i,count_sheps(x, ref))

