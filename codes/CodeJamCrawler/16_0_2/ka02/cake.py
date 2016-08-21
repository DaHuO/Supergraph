t = int(raw_input())
test = t

while t > 0:
    s = raw_input()
    l = len(s)
    re = l * '+'
    
    count = 0
    
    while s != re:
        if s[0] == '+':
            j = 1
            p = 1
            while s[j] == '+':
                p += 1
                j += 1
            s = (p * '-') + s[-(l - p):]
            #print s
        
        elif s[0] == '-':            
            j = 1
            m = 1
            
            if j == l:
                s = '+'
                #print s
            
            else:
                while s[j] == '-':
                    m += 1
                    j += 1
                    if j == l:
                        break
                if l == m:
                    s = (m * '+')
                else:
                    s = (m * '+') + s[-(l - m):]
                #print s
            
        count += 1
    print "Case #" + str(test - t + 1) + ":" + " " + str(count)
    t -= 1
