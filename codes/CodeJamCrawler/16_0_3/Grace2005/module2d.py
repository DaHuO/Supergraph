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

fr=open("C:\Users\lihua\Desktop\Google_Jam\Q16c\C-small-attempt0.in","r")
wr=open("C:\Users\lihua\Desktop\Google_Jam\Q16c\C-small-attempt0.out","w")


arraylines=fr.readlines()
case=int(arraylines[0])
result="Case #1:"+"\n"
wr.write(result)
a=str(1000000000000001)
result1=a+' 3'+' 4'+' 5'+' 6'+' 7'+' 8'+' 9'+' 10'+' 11'+"\n"
wr.write(result1)
s=list(a)
n=1
for i in range(7,0,-1):
    for j in range(7,0,-1):
        s[2*i]='1'
        s[2*j-1]='1'
        a2=''.join(s)
        result2=a2+' 3'+' 4'+' 5'+' 6'+' 7'+' 8'+' 9'+' 10'+' 11'+"\n"
        wr.write(result2)
        n=n+1
        s[2*i]='0'
        s[2*j-1]='0'
        if n==50:
            break
    if n>=50:
        break


fr.close()
wr.close()
