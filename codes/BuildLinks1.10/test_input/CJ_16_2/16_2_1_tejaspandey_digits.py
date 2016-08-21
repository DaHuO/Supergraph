#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 tejas <tejas@Bazinga>
#
# Distributed under terms of the MIT license.

res=[]
freq={}
num=[ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def subtract(x , index):

    while freq[x] > 0:
        res.append(index)
        for z in num[index] : freq[z]-=1


def main():
    testCases=int(input())
    for tc in range(testCases):

        global res,freq
        res[:]=[]
        freq.clear()

        s=input()
        for c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            freq[c]=0
        for c in s : 
            freq[c]+=1
        
        subtract('Z',0)
        subtract('W',2)
        subtract('U',4)
        subtract('X',6)
        subtract('G',8)

        subtract('O',1)
        subtract('H',3)
        subtract('F',5)


        subtract('S',7)
        subtract('I',9)

        res.sort()
        print ("Case #{}: ".format(tc+1),end='')
        for i in res:
            print (i,end='')
        print()


main()

