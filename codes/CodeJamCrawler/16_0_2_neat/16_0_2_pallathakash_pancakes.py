#-------------------------------------------------------------------------------
# Name:        pancakes.py
# Purpose:
#
# Author:      Akash
#
# Created:     09/04/2016
# Copyright:   (c) Akash 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def min_flips(stack):
    minflip=0
    for i in range(1, len(stack)):
        if stack[i]!=stack[i-1]:
            stack=flip_until(stack, i)
            minflip+=1

    if stack[0]=='-':
        minflip+=1
    return minflip

def flip_until(stack, n):
    fliprev=reversed(stack[:n])
    flipped=""
    for ch in fliprev:
        if ch=='+':
            flipped+='-'
        else:
            flipped+='+'
    return flipped+stack[n:]

print min_flips('-+')
print min_flips('-+')

fr=open(raw_input(), "r")
fw=open(raw_input(), "w")

t=int(fr.readline())
for i in range(t):
    pk=fr.readline().strip()
    fw.write("Case #"+str(i+1)+": "+str(min_flips(pk))+"\n")
fr.close()
fw.close()
print("Done")
