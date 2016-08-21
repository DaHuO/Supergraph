import re

def containsAll(str, set):
    """Check whether 'str' contains ALL of the chars in 'set'"""
    return 0 not in [c in str for c in set]

def solve(N):
    if N == 0:
        return "INSOMNIA"
    count = 1
    nn = count * N
    chars = set('0123456789')
    s = str(nn)
    while  containsAll(s, chars) == 0:
        count+=1
        nn = count * N
        s = s + str(nn)
    return nn



class CountingSheep():
    inp = open(r"C:\Users\Marcelo\Documents\Code Jam 2016\Counting Sheeps\A-large.in","r")
    out = open(r"C:\Users\Marcelo\Documents\Code Jam 2016\Counting Sheeps\A-large.out","w")
    lines = inp.readlines()
    i=1
    count=1
    while i<len(lines):
        A = [int(x) for x in re.split(" ",lines[i])]
        """B = [int(x) for x in re.split(" ",lines[i+1])]
        C = [int(x) for x in re.split(" ",lines[i+2])]"""
        out.write("Case #"+str(count)+": "+"{:}".format(solve(A[0]))+"\n")
        i+=1
        count+=1
    out.close()
    inp.close()
