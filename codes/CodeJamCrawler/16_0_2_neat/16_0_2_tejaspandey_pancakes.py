#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 tejas <tejas@Bazinga>
#
# Distributed under terms of the MIT license.

baseCase={'-':1,
          '+':0,

          '-+':1,
          '+-':2,
          '--':1,
          '++':0,

          '+++':0,  
          '++-':2,  
          '+-+':2, 
          '+--':2,
          '-++':1,
          '-+-':3,
          '--+':1 ,
          '---':1  
}   
def solve(s):
    res=0
    if len(s) == 0:
        return 0
    if len(s) <= 3:
        res+=baseCase[s]
        return res
    res+= baseCase[s[:3]]+solve('+'+s[3:])
    return res

t=int(input())
for k in range(t):
    s=input()
    process=''
    for i in s:
        if len(process) == 0:
            process+=i
        elif process[-1] != i:
            process+=i
    print ("Case #{}: {}".format(k+1,solve(process)))
    
