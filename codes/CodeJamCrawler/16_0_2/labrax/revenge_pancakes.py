
# -*- coding:utf-8 -*-

tests = int(input())
for i in range(1, tests+1):
    values = list(input())
    """
    if len(values) == 1:
        if values[0] == '+':
            print("Case #" + str(i) + ": " + str(0))
            continue
        else:
            print("Case #" + str(i) + ": " + str(1))
            continue"""
            
    curr = 0
    not_ready = True
    while not_ready:
        not_ready = False
        for n in values:
            if n == '-':
                not_ready = True
                break
        #print(not_ready, values)
        for n in range(0, len(values)):
            if values[n] != values[0]:
                t = values[0]
                if t == '-':
                    t = '+'
                else:
                    t = '-'
                curr += 1
                for k in range(0, n):
                    values[k] = t
                break
        if n == (len(values)-1) and values[0] == '-':
            t = '+'
            curr += 1
            for k in range(0, n):
                values[k] = t
            not_ready = False
    
    print("Case #" + str(i) + ": " + str(curr))
