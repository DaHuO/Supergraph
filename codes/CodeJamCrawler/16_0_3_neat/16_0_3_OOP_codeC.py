from math import sqrt
from itertools import count, islice
import random
def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if number>1000000:return True
        if not n%number:
            return number
    return True
def g(bit):
    bitx=bit-2
    # a=random.randint(0,1<<bitx-1)
    # s=list(bin(a)[2:])
    s=[0,0,0,0,0,0,0,0,0]
    while len(s)<bitx:
        s+=[random.randint(0,1)]
    random.shuffle(s)
    s=[1]+s+[1]
    s="".join(map(str,s))
    return s
def f(s):
    ret=[s]
    for i in range(2,11):
        x=int(s,i)
        p=isPrime(x)
        if p is True:
            print("Prime")
            return False
        else:
            ret.append(p)
    return ret
def e():
    while True:
        print("new")
        r=f(g(32))
        if r!=False:
            print("YEah")
            print(r)
            with open("C.out") as fd:
                for i in map(lambda x:x.split(' ')[0],fd.read().split()):
                    if r[0]==i:
                        print("DUP")
                        continue
            with open("C.out","a") as fd:
                fd.write(" ".join(map(str,r)))
                fd.write("\n")
e()
