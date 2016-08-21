test = input()
for i in range(1,test+1):
    li = [0 for m in range(0,10)]
    a = input()
    c = a
    if a == 0:
        print "Case #"+str(i)+": INSOMNIA"
    else:
        while sum(li)!=10:
            for d in str(a):
                li[int(d)] = 1
            a+=c
        print "Case #"+str(i)+": "+str(a-c)


