'''
Created on Apr 9, 2016

@author: hduser
'''


def solve(s):
    k = 0
    try:
        while (len(s) > 0):
            while (s[-1] == '+'):
                s = s[:-1]
            else:
                k += 1
                s = s.replace('+', '1').replace('-', '+').replace('1', '-')
    except IndexError:
        pass
    return k


t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    print "Case #{}: {}".format(i, solve(s))
