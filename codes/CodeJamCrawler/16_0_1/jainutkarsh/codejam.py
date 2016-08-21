t = int(raw_input())
lst = []
for _ in range(t):
    n = int(raw_input())
    d = {}
    if(n == 0):
        lst.append('INSOMNIA')
    else:
        j = 1
        while(True):
            k = n*j
            j += 1
            s = str(k);
            for i in s:
                if i not in d:
                    d[i] = 1
            if(len(d)==10):
                break
        lst.append(s)
for i in range(t):
    print "Case #%d: %s"%((i+1), lst[i])
    
        
            
        
        
