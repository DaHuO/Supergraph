

def satisfy_digits(n):                                                                          
    """                                                                                         
    >>> satisfy_digits(1)                                                                       
    10
    >>> satisfy_digits(0)                                                                       
    'INSOMNIA'
    >>> satisfy_digits(11)                                                                      
    110
    """                                                                                         
    d = [0 for x in range(0, 10)]                                                               
                                                                                                
    for t in range(1, 101):                                                                     
        k = n * t                                                                               
        n_str = str(k)                                                                          
        find = True                                                                             
        for i in n_str:                                                                         
            d[int(i)] = 1                                                                       
                                                                                                
        for i in range(0, 10):                                                                  
            if d[i] == 0:                                                                       
               find = False                                                                     
                                                                                                
        if find:                                                                                
            return k                                                                            
        elif not find and t == 100:                                                             
            return 'INSOMNIA'                                                                   
                                                                                                
    return 'INSOMNIA'                                                                           
                                                                                                
                                                                                                
if __name__ == "__main__":                                                                      
    N = raw_input().strip().split()                                                             
    N = int(N[0])                                                                               
    for i in range(0, N):                                                                       
        n = int(raw_input())                                                                    
        print "Case #" + str(i+1) + ":", satisfy_digits(n)         
