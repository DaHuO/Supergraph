#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 tejas <tejas@Bazinga>
#
# Distributed under terms of the MIT license.
import sys
sys.setrecursionlimit(3000)

possible=[]

def solve(original,construct,index):
    if index >= len(original):
        possible.append(construct)
    
    elif index==0:
        solve(original,construct+original[0],index+1)
    
    elif original[index] == construct[0]:
        solve(original,original[index]+construct,index+1)
    
    elif original[index] == construct[-1]:
        solve(original,construct+original[index],index+1)

    elif original[index] < construct[0]:
        solve(original,construct+original[index],index+1)

    elif original[index] > construct[0]:
        solve(original,original[index]+construct,index+1)


def main():
    testCases = input()
    for k in range(testCases):
        global possible
        possible=[]
        s=raw_input()
        solve(s,"",0)
        possible.sort()
        print "Case #%d: %s"%(k+1,possible[-1])

    



main()
