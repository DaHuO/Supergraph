#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Byukend
# @Date:   2016-04-09 13:48:49
# @Last Modified by:   Byukend
# @Last Modified time: 2016-04-09 13:48:49

def main():
    n = int(input())
    a = set()
    for i in range(1,n+1):
        digit = input()
        if digit == '0':
            print("Case #",i ,": INSOMNIA",sep = '')
            continue
        mul = 1
        while 1:            
            new_digit = int(digit) * mul
            new_digit = str(new_digit)
            for k in new_digit:
                a.add(k)          
                # print(a,new_digit)
                if(len(a)==10): break
            if len(a) == 10:
                    print("Case #",i ,": ",new_digit,'\n',end = '',sep = '')
                    a = set()
                    break
            mul += 1


if __name__ == '__main__':
    main()