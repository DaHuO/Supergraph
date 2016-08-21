import collections

t = int(raw_input())

for a in range(t):
    
    n = int(raw_input())
    l = []
    for b in range(2*n -1):
        temp = raw_input().split()
        l.extend(temp)

    i = 0
    fl = []
    length = len(l)
    while(i < length):
        j = 0
        count = 0
        while(j < length):
            if(l[i] == l[j]):
                count = count + 1

            #print '...'

            j = j + 1

        if((count % 2) != 0):
            fl.append(l[i])

        i = i + 1

        #print '__'

    fl1 = collections.Counter(fl)
    #print fl1.keys()
    fl2 = map(lambda k: int(k) , fl1)
    fl2.sort()

    print "Case #%s:"  %(a+1),
    
    for c in range(len(fl2)):
        print fl2[c],

    print ''
    

    
            
