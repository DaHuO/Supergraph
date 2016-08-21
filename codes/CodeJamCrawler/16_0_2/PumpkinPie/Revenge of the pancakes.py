from __future__ import division

import os
import os.path, time
import itertools

def flip(x,Line_bin):
        arr_flip=Line_bin[0:x]
        arr_rest=Line_bin[x:]
        arr_flip=arr_flip[::-1]
        arr_flip=[abs(i-1) for i in arr_flip]
        return(arr_flip+arr_rest)

def combine(Line_bin):
        j=Line_bin[0]
        New_line=[j]
        for i in range (1,len(Line_bin)):
                if Line_bin[i]!=j:
                        j=Line_bin[i]
                        New_line.append(j)
        return(New_line)
                
                
        

def numflips(Line):
        Line_bin=[]
        Line_arr=[i for i in str(Line)]
        for i in range(0,len(Line_arr)):
                if Line_arr[i]=="+":
                        Line_bin.append(1)
                if Line_arr[i]=="-":
                        Line_bin.append(0)
        simple=combine(Line_bin)
        flips=0
        while simple!=[1]:
                simple=combine(flip(1,simple))
                
                flips=flips+1
        return(flips)
        
        


#fo=open("test.txt")
#fw=open("test_out.txt","w")
#fo=open("B-small-attempt0.in")
#fw=open("B-small-attempt0.out","w")
fo=open("B-large.in")
fw=open("B-large.out","w")

n=int(fo.readline())
for k in range(0,n):
        Line=fo.readline()

        print "Case #"+ str(k+1)+": "
        print(numflips(Line))
        fw.write("Case #"+ str(k+1)+": ")
        fw.write(str(numflips(Line))+"\n")         
fw.close()        
        
                





