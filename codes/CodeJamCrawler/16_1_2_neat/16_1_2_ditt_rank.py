# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

fout = open('B-large.out', 'w')
with open('B-large.in') as f:
    T = int(f.readline())
    for case in range(T):
        N = int(f.readline().strip())
        data = []
        for line in range(2*N-1):
            data += list(map(int,f.readline().strip().split()))
        count = {item:0 for item in set(data)}
        for item in data:
            count[item] += 1
        print(count)
        missing = []
        n = 0
        while len(missing) < N:
            for item in count:
                if count[item] % 2 > 0:
                    for i in range(2**n):
                        missing.append(item)
            for item in count:
                count[item] //= 2
            n += 1
        missing.sort()
        outline = ''
        for item in missing:
            outline += ' ' + str(item)
        print('Case #'+str(case+1)+':'+outline)
        print('Case #'+str(case+1)+':'+outline, file=fout)
        #print('Case #'+str(case+1)+': '+lastWord, file=fout)
fout.close()