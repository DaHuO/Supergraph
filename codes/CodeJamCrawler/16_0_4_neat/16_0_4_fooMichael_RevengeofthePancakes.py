t = int(input())
for i in range(1, t + 1):
    s = input()    

    jm = s.rfind('-')
    if jm == -1:
        res = 0
    else:
        if s[0] == '+':
            pp = 1
            pn = 0
        else:
            pp = 0
            pn = 1    
        
        
        for j in range(1, jm + 1):
            if s[j] != s[j - 1]:
                if s[j] == '+':
                    pp += 1
                else:
                    pn += 1
        
        res = pp + pn
    
    print('Case #{}: {}'.format(i, res))
                
  

