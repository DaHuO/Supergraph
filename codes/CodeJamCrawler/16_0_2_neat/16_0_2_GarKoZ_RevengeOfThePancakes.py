#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

def notPancake(pancakes):
    newpancakes = ''
    for ele in pancakes:
        if ele == '-':
            newpancakes += '+'
        if ele == '+':
            newpancakes += '-'
    return newpancakes

def FlipPancake(pancakes, i):
    afterFlipPancakes = notPancake(pancakes[:i])[::-1] + pancakes[i:]
    return afterFlipPancakes

def checkAllHappyFaceUp(pancakes):
    return '-' not in pancakes

def SimplySearch(InputPancake):
    return Search(InputPancake, 0, {})


def Search(InputPancakes, FlipTime, SearchPath):
    #print 'Search : ' + InputPancakes + '  ,   ' + str(FlipTime) + '  ,   ' + str(SearchPath)
    
    if FlipTime >= len(InputPancakes):
        return None
    
    #if FlipTime <= 1:
    #    print InputPancakes
    #check redundant
    if InputPancakes in SearchPath:
        if FlipTime >= SearchPath[InputPancakes] :
            return None
    
    SearchPath[InputPancakes] = FlipTime
    
    #check finish
    if checkAllHappyFaceUp(InputPancakes):
        return FlipTime
    
    
    
    #print 'put  ' + InputPancakes
    #print SearchPath
    
    minFlipTime = None
    
    for i in range(1, len(InputPancakes)+1):
        #print i
        solutionFlipTime = Search(FlipPancake(InputPancakes, i), FlipTime + 1, SearchPath)
        if solutionFlipTime == None:
            continue
        if minFlipTime == None :
            minFlipTime = solutionFlipTime
        if minFlipTime > solutionFlipTime:
            minFlipTime = solutionFlipTime
    
    return  minFlipTime
            

    
    

'''
print notPancake('+')
print notPancake('-')
print notPancake('++--+-')
print FlipPancake('++--+-', 6)


print FlipPancake('--+-', 4)
print FlipPancake('+-++', 1)
print FlipPancake('--++', 2)

print Search('-', 0, {})
print Search('-+', 0, {})
print Search('+-', 0, {})
print Search('+++', 0, {})
print Search('--+-', 0, {})

'''
#print SimplySearch('-+--+++--+')
#print SimplySearch('-+--+++')

f = open("B-small-attempt1.in", "r")

T = int(f.readline())

for x in range(0, T):
    readline = f.readline()
    print "Case #" + str(x+1) + ": " + str(SimplySearch(readline))
