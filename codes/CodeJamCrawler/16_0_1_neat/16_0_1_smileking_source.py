#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jesli
# @Date:   2016-04-10 00:18:14
# @Last Modified by:   Jesli
# @Last Modified time: 2016-04-10 02:39:17
# 
import os,sys

def FindTargetNumber(number):
    maxNumber = 10000000

    numberDic = {}
    tmp = 0
    for x in xrange(1,maxNumber):
        tmp += number;
        iTmp = tmp;
        while iTmp >= 10:
            numberDic[iTmp%10] = 1
            iTmp = iTmp/10;
        numberDic[iTmp] = 1
        if len(numberDic) == 10:
            return tmp;
    return -1



file_object = open('A-large.in')
try:
    count = file_object.readlines()
    if len(count) > 0:
        reqNumber = int(count[0])
        for x in xrange(0,reqNumber):
            outNumber = FindTargetNumber(int(count[x+1]))
            if outNumber == -1:
                outNumber = "INSOMNIA"
            print "Case #"+str(x+1)+": "+str(outNumber)
finally:
    file_object.close()
