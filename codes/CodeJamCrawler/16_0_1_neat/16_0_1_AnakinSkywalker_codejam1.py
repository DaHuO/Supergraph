# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 03:48:06 2016

@author: rajbhagat
"""

fileopen = open("C:/Users/rajbhagat/Downloads/A-large.in",'r')
writefile=open("C:/Users/rajbhagat/Downloads/A-large.out",'w')
i=0
reqchars=[1,2,3,4,5,6,7,8,9,0]

for content in fileopen:
    if i>0:
        finchars=[]
        val= int(content)
        n=1
        prevlen=0
        counter=0
        while(True):
            con=str(val*n)
            
            for character in con:
                if int(character) not in finchars:
                    finchars.append(int(character))
            if len(finchars)==prevlen:
                counter+=1
            else:
                counter=0
            if len(finchars)==len(reqchars) or counter>10000:
                
                if counter>10000:
                    
                    writefile.write("Case #"+str(i)+": INSOMNIA")
                    
                else:
                    
                    writefile.write("Case #"+str(i)+": "+str(val*n))
                writefile.write("\n")
                
                break
                
            prevlen=len(finchars)
            #if str not in finchars:
                
            n+=1
                
            
    i+=1
writefile.close()