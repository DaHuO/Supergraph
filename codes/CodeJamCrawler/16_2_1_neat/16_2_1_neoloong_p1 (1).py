in1 = open('p1.in')
out1 = open('p1.out', 'w')


T = int(in1.readline())

for i in range(0, T):
    d = [0]*10
    a = [0]*26
    s = in1.readline()
    for j in range(0,len(s)-1):
        #print(s[j])
        #print(ord(s[j]))
        #print(ord('A'))
        a[ord(s[j])-ord('A')] += 1
    

    
    #ZERO
    d[0] = a[25]
    a[4] -= d[0]
    a[17] -= d[0]
    a[14] -= d[0]
    #print(d)
    
    #TWO
    d[2] = a[22]
    a[14] -= d[2]
    a[19] -=d[2]
    
    #print(d)
    #SIX
    d[6] = a[23]
    a[18] -= d[6]
    a[8] -= d[6]
    #print(d)
    
    #EIGHT
    d[8] = a[6]
    a[4] -= d[8]
    a[8] -= d[8]
    a[7] -= d[8]
    a[19] -= d[8]
    #print(d)

    
    #THREE
    d[3] = a[19]
    a[7] -= d[3]
    a[17] -= d[3]
    a[4] -= 2*d[3]
    #print(d)
    
    #FOUR
    d[4] = max(a[17],0)
    a[14] -= d[4]
    a[20] -= d[4]
    a[5] -= d[4]
    #print(d)
    
    #FIVE
    d[5] = max(a[5],0)
    a[8] -= d[5]
    a[21] -= d[5]
    a[4] -= d[5]
    #print(d)
    
    #SEVEN
    d[7] = max(a[21],0)
    a[4] -= 2*d[7]
    a[18] -= d[7]
    a[13] -= d[7]
    #print(d)
    
    #NINE
    d[9] = max(a[8],0)
    #print(d)
    
    #ONE
    d[1] = max(a[14],0)
    #print(d)
    
    out1.write("Case #%d: " %(i+1))
    
    for j in range(0,10):
        #print(d[j])
        for k in range(1,d[j]+1):
            out1.write("%d" %j)
    out1.write('\n')
    
    
in1.close()
out1.close()