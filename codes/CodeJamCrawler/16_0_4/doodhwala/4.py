for cases in range(1, int(input()) + 1):
    print('Case #%d: ' % (cases,), end='')
    k,c,s = input().split()
    k,c,s = int(k), int(c), int(s)
    
    req = 1 if c >= k else (k//c + (0 if k%c==0 else 1))
    if(s < req):
        print('IMPOSSIBLE')
    else:
        l = []
        ctr = 0
        mv = k**c
        
        for i in range(req):
            ctr += 1
            c2 = c-1
            val = 1 + c*i
            
            while(c2):
                flag = False
                if(ctr==k):
                    flag = True
                    while(c2):
                        val = (val-1)*k + 1
                        c2 -= 1
                if(not flag):        
                    val = (val-1)*k + (ctr+1)
                    ctr += 1
                    c2 -= 1
            if(val > mv):
                print('oye',val)
            l.append(min(val, mv))
        print(' '.join([str(x) for x in l]))
