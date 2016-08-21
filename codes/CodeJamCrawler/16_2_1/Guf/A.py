# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:37:18 2016

@author: zozo
"""

fname = 'A-large.in'
f = open(fname,'r')

nlines = f.readline().replace('\n','') #
inputs = []
for l in range(int(nlines)):
    inputs.append(f.readline().replace('\n',''))

f.close()

num = ["ZERO", "TWO", "SIX","EIGHT", "THREE","FOUR", "FIVE", "SEVEN", "NINE","ONE",]
digits = [0,2,6,8,3,4,5,7,9,1]

outstr = ''

for i in range(len(inputs)):
    outlist = []
    for k in range(len(num)):
        stop = 0
        while stop < 1:
            numpresent = 0
            for c in num[k]:
                if c in inputs[i] :
                        numpresent += 1
                else:
                    stop = stop + 1
                    
                        
            if len(num[k])==numpresent:
                outlist.append(digits[k])
                for kk in range(len(num[k])):
                    inputs[i] = inputs[i].replace(num[k][kk],'',1)
            else:
                stop = stop + 1
        
    outlist.sort()
    outstr += 'Case #' + str(i+1) + ': '    
    for e in outlist:    
        outstr+=str(e)
    outstr+='\n'      



fout = open(fname + '.sub','w')
fout.writelines(outstr)
fout.close()