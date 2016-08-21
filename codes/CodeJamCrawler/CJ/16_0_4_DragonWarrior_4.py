n = input()
l=[]
for i in range(n):
    a = raw_input()
    l.append(a.split(" "))

count = 1
for i in l:
    k = int(i[0])
    c = int(i[1])
    s = int(i[2])
    if(c>k):
        minclean = 1
        c = k
    else:
        minclean = k-c+1
    if(s<minclean):
        print "Case #"+str(count)+": IMPOSSIBLE"
    else:
        t = "Case #"+str(count)+": "
        if( c == 0):
            for aw in range(1,k+1):
                t = t + str(aw)+" "
        else:
            index = 0
            u = k - 1
            for a1 in range(1,c):
                index = (k * index) + (k - u)
                u = u - 1
            for aw in range(1,minclean+1):
                t = t + str(index+aw)+" "
        print t
    count = count + 1
    
            
