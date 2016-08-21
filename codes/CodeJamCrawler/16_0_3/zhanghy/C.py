# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 21:33:29 2016

@author: zhanghanyuan
"""
import sympy

l = 32
J = 500

arr = []
ansArr = [[0 for j in xrange(10)] for i in xrange(J)]
ans = [0 for i in xrange(J)]

tot = 0

g = open("C.out","w")

def dfs(x,y,limit):
    global tot,l,ans,ansArr
    
    if y == limit:
        flag = True
        w = 0
        for i in xrange(2,11):
            w = 0
            for j in xrange(l):
                w += arr[j] * (i ** j)
            t = 0
            if sympy.isprime(w):
                flag = False
                break
            if (sympy.pollard_pm1(w) == None):
                flag = False
                break
            t = sympy.pollard_pm1(w)
            ansArr[tot][i-2] = t
        if flag:
            ans[tot] = w
            g.write(str(ans[tot]))
            for j in xrange(9):
                g.write(" "+str(ansArr[tot][j]))
            g.write("\n")
            tot += 1
            print tot
    else:
        for i in xrange(x,l-1):
            if (l-1-i < limit - y):
                break
            arr[i] = 1
            dfs(i+1,y+1,limit)
            arr[i] = 0
            if (tot >= J):
                break
            
g.write("Case #1:\n")
for i in xrange(l-1):
    if ((i % 3) == 1):
        continue
    arr = [0 for j in xrange(l)]
    arr[0] = 1
    arr[l-1] = 1
    dfs(1,0,i)
    if (tot >= J):
        break


    
   
