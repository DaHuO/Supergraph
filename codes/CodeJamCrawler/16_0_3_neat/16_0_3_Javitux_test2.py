#!/usr/bin/python

from twiggy import quick_setup, log as l
from copy import deepcopy
import random

filename="data03a.txt"
outfile="out03a.txt"
GROUPS=2
DATA=[]


def getData(cases):
    global DATA

    i=0
    f=open(outfile, "a+")
    for ncase in range(cases):
        rs=(ncase+1, DATA[ncase], process(DATA[ncase]))
        l.name("getData").fields(ncase=rs[0], data=rs[1], generated=len(rs[2])).info("jamcoins found")
        f.write("Case #%d:\n" % (rs[0]))
        f.write("\n".join(rs[2])+"\n")
    f.close()

def valid(ln, number):

    n=bin(number)[2:]
    n="1%s1" % ((ln-len(n)-2)*"0"+n)

    l.name("valid").fields(mask=n).info("checking...")
    divisors=[ n ]
    for base in xrange(2, 11):
        value=int(n, base)*1.0
        divisor=base*1.0
        while divisor < value:
            if value % divisor == 0.0:
                divisors.append("%d" % divisor)
                break
            elif divisor > 100000.0:
                return False
            divisor+=1.0
        else:
            return False

    return " ".join(divisors)

def getNumber(ndigits):
    min=1
    max=(ndigits-2)**2
    n=valid(ndigits, random.randint(min,max))
    while n==False:
        n=valid(ndigits, random.randint(min,max))
        l.name("getNumber").fields(number=n).info("getting numbers")
    return n

def process(case):

    ndigits=case[0]
    qty=case[1]
    result=[]
    for n in range(qty):
        l.name("process").fields(n=n).info("searching jamcoin...")
        jamcoin=getNumber(ndigits)
        while jamcoin in result:
            jamcoin=getNumber(ndigits)
        result.append(jamcoin)
        l.name("process").fields(jamcoin=jamcoin).info("jamcoin found")

    return result


def main():
    global DATA

    quick_setup()
    lines=open(filename, "r").readlines()
    cases=int(lines[0].strip())
    for g in range(cases): DATA.append(map(int, lines[g+1].strip().split(" ")))
    lg=l.name("main")
    lg.fields(cases=cases).info("init")
    getData(cases)


if __name__ == "__main__":
    main()
