#-------------------------------------------------------------------------------
# Name:        counting_sheep.py
# Purpose:
#
# Author:      Akash
#
# Created:     09/04/2016
# Copyright:   (c) Akash 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def last_no(n):
    if n==0:
        return "INSOMNIA"

    lst=[]
    setlst=set()
    curn=n
    ct=1
    while len(setlst)!=10:
        curn=ct*n
        curns=str(curn)
        for i in range(len(curns)):
            lst.append(curns[i])
        setlst=set(lst)
        ct+=1

    return (ct-1)*n

fr=open(raw_input(), "r")
fw=open(raw_input(), "w")

t=int(fr.readline())
for i in range(t):
    n=int(fr.readline())
    fw.write("Case #"+str(i+1)+": "+str(last_no(n))+"\n")
fr.close()
fw.close()
print("Done")




