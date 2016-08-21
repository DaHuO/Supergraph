import re

def div(n):
    i = 2
    list = []
    while i < 10000:
        if n % i == 0:
            return(i)
        i = i + 1
    return -1

def dec_to_bin(x):
    return int(bin(x)[2:])

def solve(a):
    count = 0
    ns = 0
    sl = ""
    maxbin = "1"*(a[0]-2)
    while ns < a[1] and count <=int(maxbin,2):
        n = "1" + str(dec_to_bin(count)).zfill(a[0]-2) + "1"
        s = n
        x = 0
        b = 2
        while x == 0 and b <= 10:
            i = int(n, b)
            d = div(i)
            if d == -1:
                x = 1
            else:
                b+=1
                s = s + " " + str(d)
        if x ==0:
            sl = sl + "\n" + s
            ns+=1
        count+=1
    print("sl:" + sl)
    return sl

class CoinJam():
    inp = open(r"C:\Users\Marcelo\Documents\Code Jam 2016\coin jam\C-large.in","r")
    out = open(r"C:\Users\Marcelo\Documents\Code Jam 2016\coin jam\C-large.out","w")
    lines = inp.readlines()
    i=1
    count=1
    while i<len(lines):
        A = [int(x) for x in re.split(" ",lines[i])]
        """B = [int(x) for x in re.split(" ",lines[i+1])]
        C = [int(x) for x in re.split(" ",lines[i+2])]"""
        out.write("Case #"+str(count)+": "+"{:}".format(solve(A))+"\n")
        i+=1
        count+=1
    out.close()
    inp.close()