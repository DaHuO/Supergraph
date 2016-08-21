t = int(raw_input())
for a in range(t):
    s = raw_input()
    for i in range(len(s) - 1):
        if(s[i+1] >= s[0]):
            temp = s[i+1]
            if (i == (len(s) - 2)):
                sf = s[:i+1]
            else:
                sf = s[:i+1] + s[i+2:]  
            s = temp + sf
            #print s , i
        
            

    print "Case #%s: %s"  %(a+1 ,s)
    
