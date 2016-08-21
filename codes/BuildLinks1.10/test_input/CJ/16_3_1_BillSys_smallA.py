#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def process(num):
    r = input()
    p = input().split(" ")
    p = list(map(int, p))
    sonuc = ""
    while True:
            if sonuc != "":
                sonuc += " "

            sonuc += chr(65+p.index(max(p)))
            p[p.index(max(p))]-=1
            
            if sum(p) == 0:
                break
            
            big = 0
            tmp = 0
            for i in range(len(p)):
                if big<p[i]:
                    big = p[i]
                    tmp = i
                    
            p[tmp]-=1
            
            if sum(p) == 0:
                sonuc += chr(65+tmp)
                break
            
            if f1(p) == True:
                sonuc += chr(65+tmp)
            else:
                p[tmp]+=1
                    
            if sum(p) == 0:
                break
	
    return "Case #"+ str(num+1) +": " + sonuc + "\n"


		
	
def f1(a):
    for i in range(len(a)):
        if a[i] / sum(a)> 0.5:
            return False
    return True

def f2(a,b):
    return True
	    
global metin
metin=""

tnumber = int(input(""))

for num in range(0,tnumber):
	metin += process(num)


dosya = open("answerA.txt", "w")
dosya.write(metin)
dosya.close()
