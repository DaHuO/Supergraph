#!/usr/bin/python
def sleep(n):
    if n==0:
        return "INSOMNIA"
    s = ""
    i = 1
    while 1:
        m = n*i  
        s+=str(m)
        if len(set(s)) >= 10:
            return m
        i=i+1

t = int(input())
for i in range(1, t + 1):
    a = raw_input()
    a = int(a)
    print "Case #%s: %s" % (i,sleep(a))