import urllib

print( 'sdfsdf')

print(2**38)

import requests

with open('A-small-attempt0.in') as f:
    n = int(f.readline())

    for i in range(n):
        s = '1234567890'
        N = int(f.readline())
        sum = N
        if N:
            ans = 0
            while s:
                for c in str(sum):
                    if s:
                        s = s.replace(c,'')
                ans+=1
                sum += N
            print("Case #%d: %d"%((i+1),sum-N))
        else:
            print("Case #%d: INSOMNIA"%(i+1))


