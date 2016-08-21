#!/usr/bin/python

from twiggy import quick_setup, log as l

filename="ddata1.txt"
GROUPS=1
DATA=[]
for g in range(GROUPS): DATA.append([])

def getData(cases, lines):
    global DATA

    i=0
    f=open("oout1.txt", "a+")
    lg=l.name("getData")
    for ncase in range(cases):
        data=(ncase+1, process(int(lines[ncase])))
        lg.fields(ncase=data[0], number=int(lines[ncase]), process=data[1]).info("process")
        f.write("case #%d: %s\n" % data)
    f.close()


def checkDigits(digits, n):

    sn="%d" % n
    for digit in list(sn):
        if not digit in digits:
            digits+=digit
    if len("".join(digits))==10:
        return digits, n
    else:
        return digits, -1

def process(number):

    digits=[]
    for n in range(1, 1000000):
        digits, r=checkDigits(digits, n*number)
        if r >0:
            return r
    return "INSOMNIA"

def main():

    quick_setup()
    lines=open(filename, "r").readlines()
    cases=int(lines[0].strip())
    lg=l.name("main")
    lg.fields(cases=cases).info("init")
    getData(cases, lines[1:])

if __name__ == "__main__":
    main()