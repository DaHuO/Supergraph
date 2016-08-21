#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      udonko
#
# Created:     10/04/2016
# Copyright:   (c) udonko 2016
# Licence:     <your licence> python3
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def res(ch):
    if ch == "+":
        return 1
    else :
        return 0
def reversedNum(n):
    if n==0: return 1
    else: return 0
def doit(src,dst, length , till):
    #print(str(src))
    for i in range(till):
        dstindex = till-i -1
        dst[dstindex] = reversedNum( src[i])
        #print("dstindex={0} srcindex={1}, now dst[index] = {2}".format(dstindex, i, dst[dstindex]) )
    #print(str(dst))
    for i in range(till, length):
        dst[i] = src[i]
    #print(str(dst))
def resolve(line):
    length = len(line)
    count = 0
    current=[ res(ch) for ch in line ]
    back=[0 for ch in line]
    while True:
        if sum(current) == length:
            return count
        # count continuous - from first
        plusflombegin=0
        for i in range(length):
            if current[i] == 0:break
            else:plusflombegin+=1
        if plusflombegin > 0:
            doit(current, back, length, plusflombegin)
        else:
            # count continuous + from last
            plusnumfromend=0
            for i in range(length-1,-1,-1):
                if current[i] == 0:break
                else:plusnumfromend+=1
            doit(current, back, length, length - plusnumfromend)
        current, back = back, current

        count += 1

def readandwrite(infile, outfile):
    T=int(infile.readline())
    for t in range(T):
        line=infile.readline().strip()
        retval=resolve(line)
        a="Case #{0}: {1}\n".format(t+1, retval)
        outfile.write(a)

        #print(a)

def main():
    with open("B-large (1).in","r") as infile:
        with open("Revenge of the Pancakes.txt","w") as outfile:
            readandwrite(infile, outfile)

if __name__ == '__main__':
    main()
