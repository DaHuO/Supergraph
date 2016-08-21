# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:54:52 2016

@author: huisu
"""

def solution(s):
    flag = True
    count = 0
    for i in range(len(s)):
        if s[i] == '-' and flag is True:
            if i == 0:
                count += 1
            else:
                count += 2                
            flag = False
        elif s[i] == '+' and flag is False:
            flag = True
    return count
       
    
       
            
            

if __name__ == '__main__':
    fp = open('B-large.in')
    n = fp.readline()
    f = open("output", 'w+') 
    for i in range(int(n)):
        line = fp.readline()
        f.write("Case #"+str(i+1)+": "+str(solution(line))+'\n')
    fp.close()
    f.close()