import math
t = int(raw_input())
k = 1
while t:
    s = str(raw_input())
    l=['']
    x = 0
    for i in s:
        if i >= l[0]:
            l.insert(0,i)
        else:
            l.append(i)

    print "Case #"+str(k)+": "+str(''.join(l))

    k= k+1
    t = t - 1
