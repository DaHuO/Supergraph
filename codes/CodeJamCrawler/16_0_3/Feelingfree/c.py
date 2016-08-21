#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: feelingfree
# @Date:   2016-04-09 19:45:44
# @Last Modified by:   feelingfree
# @Last Modified time: 2016-04-10 00:44:00
import math
def is_coin_jam(coin):
    list_ = []
    is_valid = True
    for i in range(2, 10+1):
        num = convert_any_base_to_dec(coin, i)
        is_prime_result = is_prime(num)
        if is_prime(num) == 0:
            is_valid = False
            break
        else:
            list_.append(is_prime_result)
    return is_valid, list_

def convert_any_base_to_dec(number, base):
    str_num = str(number)
    length = len(str_num)-1
    res = 0
    for i in str_num:
        if i == '1':
            res = res + pow(base, length)
        length = length - 1
    return res

def is_prime(num):
    for i in range(int(math.sqrt(num))+1, 2-1, -1):
        if num%i == 0:
            return i
    return 0

def coin_jam_generate(length, end):
    count = 0
    for i in range(0, pow(2, length-2)):
        coin = pow(10, length - 1) + int("{0:b}".format(i)) * 10 + 1;
        is_valid, trivial_list = is_coin_jam(coin)
        if is_valid :
            print(coin, end = ' ')
            for i in trivial_list:
                print(i, end = ' ')
            print()
            count = count + 1
        if count == end:
            break
        
def main():
    T = int(input())
    for i in range(0, T):
        in_ = input()
        input_ = in_.split(' ')
        N = int(input_[0])
        J = int(input_[1])
        print('Case #{0}:'.format(i+1))
        coin_jam_generate(N, J)
if __name__ == '__main__':
    main()
