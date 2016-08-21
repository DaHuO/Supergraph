#!/usr/bin/env python

# Google Code Jam 2016
# Qualification Round
# A. Counting Sheep
# patsp

nTests = int(input())
for t in range(1, nTests + 1):
    n = int(input())
    if n == 0:
        print('Case #{0}: INSOMNIA'.format(t))
    else:
        done = False
        digitSet = set()
        targetDigitSet = set('0123456789')
        x = n
        #cnt = 0
        while not done:
            currDigitSet = set(str(x))
            #print(currDigitSet)
            digitSet |= currDigitSet
            #print(digitSet)
            if (targetDigitSet == digitSet):
                done = True
            else:
                x += n
            #cnt += 1
        #print(cnt)
        print('Case #{0}: {1}'.format(t, x))

