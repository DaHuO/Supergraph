
def solve(N):

    
    if N ==0:
        return 'INSOMNIA'
    already_used = []
    
    i = 0
    while True:
        i+=1
        currentN = i*N
        
        IntListN = set(map(lambda x : int(x),list(str(currentN))))
        IntListNewOnes = filter(lambda x : x not in already_used,IntListN)
        already_used += IntListNewOnes 
        already_used = sorted(already_used)
        
        if len(already_used) == 10:
            return str(currentN)
        


    
    


