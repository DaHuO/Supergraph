#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jesli
# @Date:   2016-04-10 00:18:14
# @Last Modified by:   Jesli
# @Last Modified time: 2016-04-10 01:14:35

import os,sys

sourceDic = {}


def excutePrint(inputStr):
    valuse = inputStr.split(' ')
    K = int(valuse[0])
    C = int(valuse[1])
    S = int(valuse[2])

    ret=""
    for x in xrange(0,S):
        ret = ret + " " + str(x+1) 
    return ret




file_obj = open('D-small-attempt0.in')
try:
    inputList = file_obj.readlines()
    if len(inputList) > 0:
        inputCount = int(inputList[0])
        for x in xrange(0,inputCount):
            print "Case #" + str(x+1) + ":" + excutePrint(inputList[x+1])
finally:
    file_obj.close()
    pass
