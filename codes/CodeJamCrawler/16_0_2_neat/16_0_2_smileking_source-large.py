#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jesli
# @Date:   2016-04-09 23:10:24
# @Last Modified by:   Jesli
# @Last Modified time: 2016-04-10 03:14:12


import os,sys
import Queue


def simpleStr(sourStr):
    ret = sourStr[0]
    for x in xrange(1,len(sourStr)):
        if sourStr[x] != ret[len(ret)-1]:
            ret = ret + sourStr[x]
    return ret;


def GenerateChange(inputStr, index):
    tmpStr = inputStr[0:index]
    subStr = inputStr[index:len(inputStr)]

    appstr = ""
    for x in xrange(0,len(tmpStr)):
        key = tmpStr[len(tmpStr) - 1 - x]
        if key == '+':
            appstr = appstr + "-"
        else:
            appstr = appstr + "+" 

    return appstr + subStr

    

def GenerateOutPut(inputStr):
    
    exactStr = inputStr.replace("\n","")
    searchQue = Queue.Queue()
    searchDic  = {}
    searchDic[simpleStr(exactStr)] = 0

    searchQue.put(simpleStr(exactStr))

    while not searchDic.has_key("+"):
        startKey = searchQue.get()
        for x in xrange(0,len(startKey)):
            tmp = GenerateChange(startKey, x+1)
            tmp = simpleStr(tmp)
            if not searchDic.has_key(tmp):
                searchQue.put(tmp)
                searchDic[tmp] = searchDic[startKey] + 1


    return searchDic["+"]



#file_obj = open('B-small-attempt0.in')
file_obj = open('B-large.in')
try:
    inputList = file_obj.readlines()
    if len(inputList) > 0:
        inputCount = int(inputList[0])
        for x in xrange(0,inputCount):
            print "Case #" + str(x+1) + ": " + str(GenerateOutPut(inputList[x+1]))
finally:
    file_obj.close()
    pass
