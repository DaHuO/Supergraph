T = input()

for i in range(T):
    n = input()
    #print "N: ", n
    if n == 0:
        print "Case #%d: INSOMNIA"%(i+1)
        
    else:
        found = 0
        f = [0,0,0,0,0,0,0,0,0,0]
        cur = n
        while found < 10:
            #print cur
            temp = cur
            while temp > 0:
                if f[temp%10] == 0:
                    found += 1
                    f[temp%10] = 1
                temp = temp/10
        
            if found == 10:
                break
        
            cur += n
                
        print "Case #%d: %d"%(i+1, cur)
