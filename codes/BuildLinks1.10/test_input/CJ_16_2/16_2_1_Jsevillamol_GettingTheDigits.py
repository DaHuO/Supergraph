# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:20:17 2016

@author: Jaime
"""

from collections import defaultdict

numbers = [ ("ZERO",'Z', 0),("TWO", 'W', 2), 
            ("SIX", 'X', 6), ("EIGHT", 'G', 8), 
            ("SEVEN", 'S', 7), ("FIVE", 'V', 5),
            ("FOUR", 'F', 4), ('THREE', 'R', 3),
            ("NINE", 'I', 9), ("ONE", 'O', 1)]

def solve_case(string):
    freq = defaultdict(int)
    res = [0 for i in range(10)]
    for char in string:
        freq[char]+=1
    
    for name, special_char, value in numbers:
        while(freq[special_char]>0):
            res[value]+=1
            for char in name:
                freq[char]-=1
    
    phone = "".join([str(i)*res[i] for i in range(10)])
    
    return phone

with open("in.data") as data, open("out.txt", 'w') as out:
    data.readline()
    i=1
    for line in data:
        out.write("CASE #"+str(i)+": "+solve_case(line)+'\n')
        i+=1