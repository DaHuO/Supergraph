'''
Created on 9 Apr 2016

@author: szalivako
'''

T = int(raw_input())
for ti in xrange(T):
    s = raw_input()
    intervals = 1
    for i in xrange(1, len(s)):
        if (s[i] != s[i - 1]):
            intervals += 1
    
    if (s[-1] == '-'):
        ans = intervals
    else:
        ans = intervals - 1
    
    print 'Case #' + str(ti + 1) + ': ' + str(ans)
        