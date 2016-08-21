#!/usr/bin/python
input = open("A-large.in")
T = int(input.readline())
for t in range(T):
    start_i = int(input.readline())
    if start_i == 0:
        print "Case #%s: INSOMNIA" % (t+1)
        continue
    res=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ans = start_i
    while True:
        number = ans 
        while number:
            digit = number % 10
            number = number / 10
            res[digit] = 1
        if 0 not in res:
            print "Case #%s: %s" % (t+1, ans)
            break
        ans += start_i
