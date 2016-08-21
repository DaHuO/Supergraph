#!/usr/bin/env python

n = int(input())

printlist = []

for i in range(n):
    num = int(input())
    
    if(num == 0):
        printlist.append("Case #{}: INSOMNIA".format(i+1))
    else:
        d = {}
        x = num
        k = 1
        while(len(d) < 10):
            x = num*k # most recent number
            
            for c in str(x):
                if( c not in d):
                    d[c] = 1
                else:
                    d[c] = d[c] + 1

            k += 1

        # now d has all digits
        printlist.append("Case #{}: {}".format(i+1, x))

for i in range(len(printlist)):
    print(printlist[i])


    
    
        
    
    
