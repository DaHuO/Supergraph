#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: feelingfree
# @Date:   2016-04-09 15:41:57
# @Last Modified by:   feelingfree
# @Last Modified time: 2016-04-09 18:25:52
def make_happy(pancake):
    #print('T Case : {0}'.format(pancake))

    count = 0
    while pancake.find('-') != -1: 
        if pancake[0] != '+' and pancake[-1] == '-': # -xxx-
            pancake = flip(pancake, len(pancake))
        elif pancake[0] == '+' and pancake[1:].find('+') == -1: # +----
            pancake = flip(pancake, 1)
        elif pancake.find('+') == -1: # -----
            pancake = flip(pancake, len(pancake))
        elif pancake[:2] == '+-': # +-++
            pancake = flip(pancake, 1)
        elif pancake[0] == '+' and pancake[1:].find('-') != -1:
            count_happy = 0
            for i in range(0, len(pancake)):
                if pancake[i] == '+':
                    count_happy = count_happy + 1
                else:
                    break
            pancake = flip(pancake, count_happy)
        else:
            count_happy = 0
            for i in range(len(pancake) - 1, 0, -1 ):
                if pancake[i] == '+':
                    count_happy = count_happy + 1
                else:
                    break
            pancake = flip(pancake, len(pancake) - count_happy)

        count = count + 1
        #print(pancake ,count)
    return count
        

def flip(pancake,length):
    list_pancake = []
    not_flip = pancake[length:]
    for i in range(0, length):
        list_pancake.append(pancake[i])
    return flip_swap(list_pancake) + not_flip


def flip_swap(list_pancake):
    result = ''
    list_pancake.reverse()
    for i in list_pancake:
        result = result + swap(i)
    return result

def swap(s):
    if s == '-':
        return '+'
    else:
        return '-'
def main():
    list_s = []
    count = 1
    T = int(input())
    for i in range(0, T):
        s = input()
        list_s.append(s)
    for s in list_s:
        print('Case #{0}: {1}'.format(count,make_happy(s)))
        # print('---------------------')
        count = count + 1
if __name__ == '__main__':
    main()