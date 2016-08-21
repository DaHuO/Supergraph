import sets
import copy
import time

inp = open("alarge.txt",'r').read()

"""4
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER"""

nums = ["ZERO",
        "ONE", 
        "TWO",
        "THREE",
        "FOUR",
        "FIVE",
        "SIX",
        "SEVEN",
        "EIGHT",
        "NINE"]

DEBUG=False

def remove(s1,s2):
    s3 = list(copy.copy(s1))
    if DEBUG:
        print s3 
    for c in s2:
        if c in s3:
            del s3[s3.index(c)]
        else:
            if DEBUG:
                print c,
                print " not found in ",
                print s3
            return False
    if DEBUG:
        print "FOUND!"
    if len(s3)>0:
        return "".join(s3)
    else:
        return ""
        
encoding = copy.copy(nums)        
import random
inp = inp.split("\n")
N = inp[0]
f = open("output.txt",'w')
iter=1
for l in inp[1:-1]:
    ans = []
    L = copy.copy(l)
    while len(l)>0:
        for n in nums:
            lp = remove(l,n)
            if DEBUG:
                print "Checking %s -> %r"%(n,True if lp else False)
            if not lp == False:
                if DEBUG:
                    print "REMOVE %s from %s -> %s"%(n,l,lp)
                l = lp
                ans.append(encoding.index(n))
                break
            elif n==nums[-1]:
                if DEBUG:
                    print "RESTART"
                random.shuffle(nums)
                ans = []
                l=L
            if DEBUG:
                time.sleep(.1)
    f.write("Case #%d: "%(iter)+"".join(map(lambda n: str(n),sorted(ans)))+"\n")
    iter+=1
            
