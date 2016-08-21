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

fr=open("C:\Users\lihua\Desktop\Google_Jam\Q16b\B-large.in","r")
wr=open("C:\Users\lihua\Desktop\Google_Jam\Q16b\B-large.out","w")


arraylines=fr.readlines()
case=int(arraylines[0])
for i in range(1,case+1):
    st=list(arraylines[i])
    n=len(st)
    if st[n-2]!='+':
        x=1
    else:
        x=0
    for j in range(1,n-1):
        if st[j]!=st[j-1]:
            x=x+1
        else:
            continue

    print arraylines[i], x


    result="Case #"+str(i)+": "+str(x)+"\n"
    wr.write(result)

fr.close()
wr.close()
