def remove_all(s,d,count):
    for c in d:
        s = s.replace(c, "",count)
    return s
def countn(s):
    d = dict(zip(range(10),[0]*10))
    d[0] = s.count("Z")
    s = remove_all(s,"ZERO",d[0])
    d[2] = s.count("W")
    s = remove_all(s,"TWO",d[2])
    d[4] = s.count("U")
    s = remove_all(s,"FOUR",d[4])
    d[6] = s.count("X")
    s = remove_all(s,"SIX",d[6])
    d[8] = s.count("G")
    s = remove_all(s,"EIGHT",d[8])
    
    d[1] = s.count("O")
    s = remove_all(s,"ONE",d[1])
    d[3] = s.count("H")
    s = remove_all(s,"THREE",d[3])
    d[5] = s.count("F")
    s = remove_all(s,"FIVE",d[5])
    d[7] = s.count("S")
    s = remove_all(s,"SEVEN ",d[7])
    d[9] = len(s)/4
    
    rets = ""
    for k in range(10):
        rets += str(k)*d[k]
    return rets
    
t = int(raw_input())
for i in range(t):
    s = raw_input()
    print "Case #{}: {}".format(i+1, countn(s))
