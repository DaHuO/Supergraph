y=input()
for j in range(0,y):
    x=raw_input()
    s=x[0]
    for i in x[1:]:
        if i>=s[0]:
            s=i+s
        else:
            s=s+i
    print "Case #%s:" % (j),
    print s