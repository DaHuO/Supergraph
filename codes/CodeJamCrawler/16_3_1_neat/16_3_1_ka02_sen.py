t = int(raw_input())
test = t
x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def get_weight(l, s):
    global g
    b = []
    for i in l:
        b.append((i / float(s)) * 100)
        
    
    return b, b.index(max(b)), max(b)
        
while t > 0:
    g = []
    n = int(raw_input())
    a = map(int, raw_input().split())
    #print a
    s = sum(a)
    #print a, s
    while s != 0:
        s = sum(a)
        if s != 0:
            c, m, i1 = get_weight(a, s)
            a[m] = a[m] - 1
            #print c
            c2, m2, i2= get_weight(a, sum(a))            
            #print i2, c2
            if i2 > 50:
                a[m2] = a[m2] - 1
                s = sum(a)
                #ss = str(m) + str(m2)
                ss = x[m] + x[m2]
            else:
                ss = x[m]
            g.append(ss)
        else:
            break
        #print m, g, a, len(g)
        
    #x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    st = ''
    for i in g:
        st = st + ' ' + i
    #print "->" + str(g)
    print "Case #" + str(test - t + 1) + ":" + " " + st
    t -= 1