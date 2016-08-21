f = [line.rstrip() for line in open('/Users/roshil/Desktop/A-small-attempt1.in')]
out = open('/Users/roshil/Desktop/out.txt','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for i in range(1, testcases+1):
    r1 = int(f[line])
    line += 1
    l = [int(a) for a in f[line].split()]
    line += 1
    
    loop = True
    #loop = False
    ans = []
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while loop == True:
        m = max(l)
        if m==0:
            break
        mind = l.index(m)
        l[mind] = m-1
        n = max(l)
        nind = l.index(n)
        if m > n:
            ans.append(str(alpha[mind]))
        #print 'gogo'
        elif m==n and m>1:
            ans.append(str(alpha[mind]) + str(alpha[nind]))
            #print 'yoyo'
            l[nind] = n-1
        elif sum(l) > 1:
            ans.append(str(alpha[mind]))
        #print 'yoyo'
        else:
            ans.append(str(alpha[mind]) + str(alpha[nind]))
            l[nind] = n-1
    #print 'lolo'
    #print l
    ans = ' '.join(ans)
    print ans
    
    out.write("Case #"+str(i)+": "+str(ans) + "\n")
out.close()