

T = int(input())


for t in range(T):
    
    N = int(input())
    
    if not N:
        print("Case #%d: INSOMNIA" % (t+1))
        continue
    
    seen = []
    i = 1
    while i < 1000:
        
        digits = str(i*N)
        
        for digit in map(int, digits):
            if digit not in seen:
                seen.append(digit)
        
        if len(seen) == 10:
            break
        
        i += 1
    
    if i >= 1000:
        print("Case #%d: INSOMNIA" % (t+1))
    else:
        print("Case #%d: %d" % (t+1, i*N))



