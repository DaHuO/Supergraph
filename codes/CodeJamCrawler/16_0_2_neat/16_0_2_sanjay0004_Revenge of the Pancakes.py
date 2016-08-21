t = int(raw_input())
l = []

for b in range(t):
    temp = raw_input()
    #print temp
    l.append(temp)

    
for a in range(t):
    s = l[a]
    #print s

    i = 0
    n = 0
    while(1):
        
        i = i + 1
        try :
            s[i]
        except IndexError:
            break
        else:
            if s[i] != s[i - 1] :
                n = n + 1

    if(s[0] == '-'):
        if((n%2) == 0):
            t = n + 1
        else:
            t = n

    else :
        if((n%2) == 0):
            t = n
        else:
            t = n + 1

    print "Case #%s: %s"  %(a+1 ,t)

