# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 23:15:13 2016

@author: mythcard
"""


def get_flip_count(input1):
    lst1 = list(input1)
    lst1.pop()
#    print("List details: ",lst1)
    flip = 0
    while len(lst1) > 0:
        if lst1[len(lst1) - 1] == '+':
            lst1.pop()
        else:
            flip = flip + 1
            for i in range(0,len(lst1)):
                if lst1[i] == '+':
                    lst1[i] = '-'
                else:
                    lst1[i] = '+'
    return flip   
    
#print(get_flip_count(input1))


f = open("B-large.in",'r')
k = open("output12.out",'w')
count1 = int(f.readline())

for case_n in range(1,count1 + 1):
    input1 = f.readline()
#    print("Input: ",input1)
    k.writelines("Case #")
    k.writelines(str(case_n))
    k.writelines(": ")
    k.writelines(str(get_flip_count(input1)))
    k.writelines("\n")
    
f.close()  
k.close()