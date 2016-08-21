#!/usr/bin/python

from twiggy import quick_setup, log as l
from copy import deepcopy

filename="data02b.txt"
outfile="oout02b.txt"
GROUPS=2
DATA=[]


def getData(cases, lines):
    global DATA

    i=0
    f=open(outfile, "a+")
    for ncase in range(cases):
        rs=(ncase+1, DATA[ncase], process(DATA[ncase]))
        l.name("getData").fields(ncase=rs[0], data=rs[1], switches=rs[2]).info("switches found")
        f.write("Case #%d: %d\n" % (rs[0], rs[2]))
    f.close()

def checkCorrect(case):
    return "-" not in list(case)

def group(case):
    gcase=""
    cur=""
    cn=0
    while cn<len(case):
        cur=case[cn]
        gcase+=cur
        while cn<len(case) and cur==case[cn]:
            cn+=1

    return gcase

def process(case):

    if checkCorrect(case):
        return 0

    gcase=group(case)
    switches=len(gcase)-1
    if gcase[-1]=="-":
        switches+=1

    return switches

def main():
    global DATA

    quick_setup()
    lines=open(filename, "r").readlines()
    cases=int(lines[0].strip())
    for g in range(cases): DATA.append(lines[g+1].strip())
    lg=l.name("main")
    lg.fields(cases=cases).info("init")
    getData(cases, lines[1:])


if __name__ == "__main__":
    main()
