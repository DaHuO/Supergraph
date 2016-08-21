# -*- coding: utf-8 -*-
######################################################
##                                                  ##
##  Fran Muñoz                                      ##
##  email: fran.mzy@gmail.com                       ##
##  UVA user: franmzy                               ##
##  Linkedin: https://www.linkedin.com/in/franmzy   ##
##                                                  ##
######################################################

n_cases = int(input())

for i_case in range(n_cases):
    K, C, S = list(map(int, input().split()))
    print('Case #{0}:'.format(i_case+1), end=" ")

    for i in range(K-1):
        print( i * (K**(C-1)) + 1, end = " ")
    print( (K-1) * (K**(C-1)) + 1)
