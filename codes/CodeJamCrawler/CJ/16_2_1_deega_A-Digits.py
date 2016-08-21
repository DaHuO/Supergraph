#!/usr/bin/env python3
def counter(s):
    o = []
    for i in s:
        o.append(count.get(i,0))
    return min(o)
def check():
    for i in count.values():
        if i > 0:
            return False
    return True
T = int(input())
for i in range(T):
    s = input()
    count = {}
    out = []
    for j in s:
        count[j] = count.get(j,0) + 1
    a = [('ZERO',0), ('TWO',2), ('FOUR',4), ('SIX',6),
         ('EIGHT',8), ('THREE',3), ('FIVE',5), ('ONE',1),
         ('SEVEN',7), ('NINE',9)]
    for j in a:
        temp = counter(j[0])
        if temp > 0:
            for k in j[0]:
                count[k] -= temp
            out.extend([j[1]] * temp)
    if check():
        out.sort()
        print('Case #{}: {}'.format(i+1,''.join(map(str,out))))
