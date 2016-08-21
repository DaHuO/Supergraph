'''
Created on 9 Apr 2016

@author: toby8
'''

with open("B-Large.in" , "r") as fin:
    filein = fin.read().splitlines()
filein.pop(0)

print filein

times = 1
with open("output.in" , "w") as fout:
    for s in filein:
        if s[-1] == '+':
            current = '+'
            count = 0
            for c in reversed(s):
                if c != current:
                    current = c
                    count += 1
            print count
            str1 = "Case #%s: %s\n" % (times, count)
            fout.write(str1)
            
        if s[-1] == '-':
            count = 1
            current = '-'
            for c in reversed(s):
                if c != current:
                    current = c
                    count += 1
            print count
            str1 = "Case #%s: %s\n" % (times, count)
            fout.write(str1)
    
        times+=1