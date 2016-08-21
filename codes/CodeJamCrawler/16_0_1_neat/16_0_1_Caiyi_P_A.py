# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 19:06:53 2016

@author: caiyi
"""

"""
counting sheep
"""
def write_res(file_name, res):
    with open(file_name,'w') as f:
        res_str = ''
        for i in range(len(res[:-1])):
            res_str += "Case #{}: ".format(i+1)+ str(res[i])+'\n'
        res_str += "Case #{}: ".format(i+2) + str(res[-1])
        f.write(res_str)


def func(num):
    """
    return the last number before sleep, if never stop, return INSOMNIA
    """
    S = set([str(i) for i in range(10)])
    i = 1
    
    flag = 0
    #n = num
    while i < 100000:
        n  = i * num
        #print n
        for l in str(n):
            if l in S:
                S.remove(l)
        if len(S) == 0:
            flag = 1
            break
        i += 1
        
        if (n > 2**31 - 1) and i > 100 :
            break

        
    if flag == 1:
        return n
    else:
        return "INSOMNIA"
    
#l = [0,1,2,11,1692]
#for i in l:
#    #print i
#    print func(i)


#l = [0,1,2,11,1692]

with open('A-large.in') as f:
    str1 = f.read()
    l = [int(ch) for ch in str1.strip().split('\n')[1:]]
    
res = []
for num in l:    
    #num = int(ch)
    print "the num", num
    
    tmp = func(num)
    print 'the result ', tmp
    #print tmp
    res.append(tmp)
    
write_res('res_A_large.txt', res)
        
    
    

    
    