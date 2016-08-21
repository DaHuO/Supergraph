#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def process(num):

    text = input()
    #text = list(map(str, text))
    
    #if len(text)!=2  :
        #return

    #smax = int(text[0])
    #kvalues = str(text[1])
   
    #if (smax > smax_val) | (smax < smin_val):
       # return
    
  
    #if ((len(kvalues)-1) != smax):
       # print(kvalues)
        # return
    
    total_clap = 0
    invite = 0
    
    #for s,k in enumerate(kvalues):
        
     #   if k!=0:
      #      while s > total_clap:
       #         total_clap +=1
        #        invite +=1

        #total_clap += int(k)

    f = []
    for i in range(10):
       f.append(0)

    a = 1
    lm = int(text)
    if lm>smax_val and lm < smin_val:
        invite = ""
    else:
        while True:
            con = True
            res = a*int(text)
            res = str(res)
            for x in range(0, len(res)):
                f[int(res[x])] = 1
            
            for x in range(0, len(f)):
                if f[x] == 0:
                    con = False
                    break
            
            if con:
                invite = res
                break
            a = a+1
            if a == 200:
                invite = "INSOMNIA"
                break
        

    return "Case #"+ str(num+1) +": " +str(invite) + "\n"
            
            

global tmax
global tmin
global smax_val
global smin_val

tmax = 100
tmin = 1
smax_val = math.pow(10,6)
smin_val = 0


global metin
metin=""

tnumber = int(input(""))
#print(str(tnumber))
if (tnumber <= tmax) & (tnumber >= tmin):
    for num in range(0,tnumber):
        metin += process(num)


dosya = open("answer.txt", "w")
dosya.write(metin)
dosya.close()
