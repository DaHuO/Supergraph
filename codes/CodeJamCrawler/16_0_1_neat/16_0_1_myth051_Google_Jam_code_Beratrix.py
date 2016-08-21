# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:48:33 2016

@author: mythcard
"""
import sys

lst = [0,1,2,3,4,5,6,7,8,9]

def get_fall_asleep_number(number,lst):
    cnt = 1
    number2 = 0
    if number == 0:
        return 'INSOMNIA'
    while len(lst) != 0:
        lst1 = []
        number2 = cnt * number
        number1 = number2
        while number1:
            digit = number1 % 10
            lst1.append(digit)
            number1 //= 10
    
        for item in lst1:
            if item in lst:
                lst.pop(lst.index(item))
            
        cnt = cnt + 1        
        
    return number2
        
status = 0

f = open("A-large.in",'r')
k = open("output.out",'w')
number = f.readline()
while number != '':
    print(number)
    number = int(number)
    if status == 0:
        status = status + 1
        number = f.readline()
        continue
    k.writelines("Case #")
    k.writelines(str(status))
    k.writelines(": ")
    k.writelines(str(get_fall_asleep_number(number,lst[:])))
    k.writelines("\n")
    status = status + 1
    number = f.readline()
f.close()  
k.close()  
    
            