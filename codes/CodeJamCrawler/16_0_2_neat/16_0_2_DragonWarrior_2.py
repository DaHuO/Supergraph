n = input()
l = []



for i in range(0,n):
    l.append(raw_input())

o = 1
for t in l:
    x = list(t)
    x.reverse()
    count = 0
    while(len(x)!=0 and x[0] == '+'):
            del x[0]
    if(len(x)!=0):
        type = x[0]
        if(type == '-'):
            count = 1
        for a in range(1,len(x)):
            if(type != x[a]):
                type = x[a]
                count = count + 1
    print "Case #"+str(o)+": "+str(count)
    o = o+1     
