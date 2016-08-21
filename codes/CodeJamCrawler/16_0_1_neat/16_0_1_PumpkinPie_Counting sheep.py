from __future__ import division

import os
import os.path, time
import itertools

def lastnum(ST):
        numbers_tot=[]
        orig=ST
        k=1
        while True:
                numbers_app=[int(i) for i in str(ST)]
                numbers_tot=numbers_tot+numbers_app
                numbers_tot=list(set(numbers_tot))
                k=k+1     
                if len(numbers_tot)==10:
                        
                        return (str(ST))
                if k==100:
                        return ("INSOMNIA")
                ST=ST+orig
                
        return(ST)
        
        


#fo=open("test.txt")
#fw=open("test_out.txt","w")
fo=open("A-large.in")
fw=open("A-large.out","w")

n=int(fo.readline())
for k in range(0,n):
        Line=fo.readline().split()
        ST=int(Line[0])
        final=lastnum(ST)
        print "Case #"+ str(k+1)+": "
        print final
        fw.write("Case #"+ str(k+1)+": ")
        fw.write(final+"\n")         
fw.close()        
        
                





