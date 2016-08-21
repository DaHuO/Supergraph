import sys

ALLNUM = set("0123456789")
def calc(x):
    if x == 0: return "INSOMNIA" 
    count = 1 
    x1 = x
    sls = "" 
    while True:
        x1 = x * count
        sx1 = str(x1)
        ls = set(sx1 + sls)
        sls = "".join(ls)
        if ls == ALLNUM:  
            return sx1 
        count += 1

num = int(raw_input())
for i in xrange(num):
    x = int(raw_input())
    print "Case #{}: {}".format(i+1, calc(x)) 

