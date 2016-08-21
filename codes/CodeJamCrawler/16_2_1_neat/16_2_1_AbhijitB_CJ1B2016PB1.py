# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 21:19:18 2016

@author: abhibhat
"""
def CJ1B2016PB1(word):
    table = [("Z" , 0 , "ZERO"),("W" , 2 , "TWO"),("U" , 4 , "FOUR"),
             ("O" , 1 , "ONE"),("X" , 6 , "SIX"),("G" , 8 , "EIGHT"),
             ("T" , 3 , "THREE"),("F" , 5 , "FIVE"),("V" , 7 , "SEVEN"),
             ("N" , 9 , "NINE")]
    numbers = []
    for item in table:
        while item[0] in word:
            for ch in item[2]:
                word = word.replace(ch, "", 1)
            numbers.append(item[1])
    return ''.join(map(str, sorted(numbers)))
T = input()
for i in range(1, T+1):
    print "Case #{}: {}".format(i, CJ1B2016PB1(raw_input()))
