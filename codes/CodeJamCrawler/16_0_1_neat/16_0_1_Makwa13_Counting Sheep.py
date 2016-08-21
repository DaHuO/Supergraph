#-------------------------------------------------------------------------------
# Name:        Counting Sheep
# Purpose:
#
# Author:      udonko
#
# Created:     09/04/2016
# Copyright:   (c) udonko 2016
# Licence:     <your licence>
#縲python3
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def resolve(n):
    if n == 0:
        return "INSOMNIA"
    flags = [0 for i in range(10)]
    multiple=1
    while True:
        ret=d=n * multiple
        while d != 0:
            d,m = divmod(d,10)
            flags[m] = 1
        if sum(flags) == 10:
            return str(ret)
        multiple+=1
def readandwrite(infile, outfile):
    T=int(infile.readline())
    for i in range(T):
        N=int(infile.readline())
        retval=resolve(N)
        a="Case #{0}: {1}\n".format(i+1, retval)
        outfile.write(a)


def main():
    with open("A-large.in","r") as infile:
        with open("outputCountingSheep.txt","w") as outfile:
            readandwrite(infile, outfile)

if __name__ == '__main__':
    main()
