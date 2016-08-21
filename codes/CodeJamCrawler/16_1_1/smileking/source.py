#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jesli
# @Date:   2016-04-10 00:18:14
# @Last Modified by:   Jesli
# @Last Modified time: 2016-04-16 09:17:37
# 
import os,sys
sys.setrecursionlimit(1000000) 

def GetLastWord(orighString):
    if len(orighString) == 1:
        return orighString
    else:
        next = GetLastWord(orighString[:-1])
        key = orighString[len(orighString)-1]
        if key >= next[0]:
            return key+next;
        else:
            return next+key;


file_object = open('A-large.in')

try:
    count = file_object.readlines()
    if len(count) > 0:
        reqStr = int(count[0])
        for x in xrange(0,reqStr):
            inStr = count[x+1][:-1]
            LastWord = GetLastWord(inStr)
            print "Case #"+str(x+1)+": "+LastWord
finally:
    file_object.close()
