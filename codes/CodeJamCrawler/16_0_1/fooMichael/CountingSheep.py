t = int(input())  
for i in range(1, t + 1):    
    n = int(input())

    if n == 0:
        res = 'INSOMNIA'
    else:
        v = set() 
        j = 1
        while True:
            res = n * j            
            res2 = res            
            while res2 > 0:
                m = res2 % 10
                res2 //= 10
                v.add(m)                
                
            if len(v) == 10:
                break
            j += 1
    
    print('Case #{}: {}'.format(i, res))
                
  

