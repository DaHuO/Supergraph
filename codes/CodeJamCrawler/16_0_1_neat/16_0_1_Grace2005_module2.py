#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      lihua
#
# Created:     08/04/2016
# Copyright:   (c) lihua 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

fr=open("C:\Users\lihua\Desktop\Google_Jam\Q16a\A-small-attempt0.in","r")
wr=open("C:\Users\lihua\Desktop\Google_Jam\Q16a\A-small-attempt0.out","w")


arraylines=fr.readlines()
case=int(arraylines[0])
for i in range(1,case+1):
    n=int(arraylines[i])
    if n==0:
        tt='INSOMNIA'
    a=list(str(n))
    targ=['0','1','2','3','4','5','6','7','8','9']
    for j in range(2,101):
        b=list(str(n*j))
        a=list(set(a+b))
        a.sort()
        if a==targ:
            tt=str(n*j)
            break



    result="Case #"+str(i)+": "+str(tt)+"\n"
    wr.write(result)

fr.close()
wr.close()
