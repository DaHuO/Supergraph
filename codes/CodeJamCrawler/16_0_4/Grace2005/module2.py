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

fr=open("C:\Users\lihua\Desktop\Google_Jam\Q16d\D-small-attempt0.in","r")
wr=open("C:\Users\lihua\Desktop\Google_Jam\Q16d\D-small-attempt0.out","w")


arraylines=fr.readlines()
case=int(arraylines[0])
for i in range(1,case+1):
    a=arraylines[i].split(' ')
    K=int(a[0])
    C=int(a[1])
    S=int(a[2])

    st='1'
    for j in range(1,K):
        st=st+' '+str(j*K**(C-1)+1)



    result="Case #"+str(i)+": "+st+"\n"
    wr.write(result)

fr.close()
wr.close()
