t = input()

for tc in range(1, t+1):
    t = [0] * 26
    a = [0] * 10
    s = raw_input()
    for i in range(0, len(s)):
        t[ord(s[i])-65] += 1
    
    a[0] = t[ord("Z")-65]
    t[ord("E")-65] -= t[ord("Z")-65] 
    t[ord("R")-65] -= t[ord("Z")-65] 
    t[ord("O")-65] -= t[ord("Z")-65] 
    
    a[8] = t[ord("G")-65]
    t[ord("E")-65] -= t[ord("G")-65] 
    t[ord("I")-65] -= t[ord("G")-65] 
    t[ord("H")-65] -= t[ord("G")-65]
    t[ord("T")-65] -= t[ord("G")-65]
    
    a[6] = t[ord("X")-65]
    t[ord("S")-65] -= t[ord("X")-65] 
    t[ord("I")-65] -= t[ord("X")-65] 
    
    a[7] = t[ord("S")-65]
    t[ord("E")-65] -= 2*t[ord("S")-65] 
    t[ord("V")-65] -= t[ord("S")-65]
    t[ord("N")-65] -= t[ord("S")-65]
    
    a[3] = t[ord("H")-65]
    t[ord("T")-65] -= t[ord("H")-65] 
    t[ord("E")-65] -= 2*t[ord("H")-65] 
    t[ord("R")-65] -= t[ord("H")-65]
    
    a[5] = t[ord("V")-65]
    t[ord("F")-65] -= t[ord("V")-65] 
    t[ord("I")-65] -= t[ord("V")-65]
    t[ord("E")-65] -= t[ord("V")-65] 
    
    a[4] = t[ord("F")-65]
    t[ord("O")-65] -= t[ord("F")-65] 
    t[ord("R")-65] -= t[ord("F")-65] 
    
    a[2] = t[ord("W")-65]
    t[ord("T")-65] -= t[ord("W")-65] 
    t[ord("O")-65] -= t[ord("W")-65]
    
    a[9] = t[ord("I")-65]

    a[1] = t[ord("O")-65]
    
    i = 0
    r = ""
    
    
    while i != 10:
        while a[i] != 0:
            r += str(i)
            a[i] = a[i]-1
        i = i + 1
            
        
    print "Case #%d: %s" % (tc,r)