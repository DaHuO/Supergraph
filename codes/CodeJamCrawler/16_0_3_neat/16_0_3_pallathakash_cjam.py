#-------------------------------------------------------------------------------
# Name:        cjam.py
# Purpose:
#
# Author:      Akash
#
# Created:     09/04/2016
# Copyright:   (c) Akash 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def convertbase(binary, base):
    num=0
    for i in range(0, len(binary)):
        num+=int(binary[i])*(base**(len(binary)-1-i))
    return num

def is_prime(n):
    if n==2:
        return [True, 1]

    divisor=1
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            divisor=i
            return[False, divisor]

    return[True,divisor]

n=16
j=50

found_coins=0

cur=2**(n-1)+1

f=open(raw_input(), "w")

print "Case #1"

while found_coins<j and cur<2**n:
    jamcoin=bin(cur)[2:]

    is_cur_jamcoin=True

    lstproofs=[]

    for base in range(2, 11):
        to_check=convertbase(jamcoin, base)
        ip=is_prime(to_check)
        if ip[0]:
            is_cur_jamcoin=False
            break
        else:
            lstproofs.append(str(ip[1]))

    if is_cur_jamcoin:
        found_coins+=1
        strp= jamcoin+" "+" ".join(lstproofs)
        print strp
        f.write(strp+'\n')

    cur+=2

print "Found "+str(found_coins)





