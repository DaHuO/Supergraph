#!/usr/bin/python

f = open('in.txt')

i = 0

for line in f:
    i += 1
    if i == 1:
        continue
    cur = int(line)
    if cur == 0:
        print 'Case #' + str(i-1) + ': INSOMNIA'
        continue
    ps = 'Case #' + str(i-1) + ': '
    mul = 1
    total = cur
    found = ''
    while 1:
        s = str(total)
        total += cur
        if '0' in found:
            a = 1
        elif '0' in s:
            found += '0'
        if '1' in found:
            a = 1
        elif '1' in s:
            found += '1'
        if '2' in found:
            a = 1
        elif '2' in s:
            found += '2'
        if '3' in found:
            a = 1
        elif '3' in s:
            found += '3'
        if '4' in found:
            a = 1
        elif '4' in s:
            found += '4'
        if '5' in found:
            a = 1
        elif '5' in s:
            found += '5'
        if '6' in found:
            a = 1
        elif '6' in s:
            found += '6'
        if '7' in found:
            a = 1
        elif '7' in s:
            found += '7'
        if '8' in found:
            a = 1
        elif '8' in s:
            found += '8'
        if '9' in found:
            a = 1
        elif '9' in s:
            found += '9'
        
        if '0' in found and '1' in found and '2' in found and '3' in found and '4' in found and '5' in found and '6' in found and '7' in found and '8' in found and '9' in found:
            ps = ps + s
            print ps
            break
