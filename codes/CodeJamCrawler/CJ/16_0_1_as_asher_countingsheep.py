T = int(input())
for t in range(T):
    N = int(input())
    if N <= 0:
        print('Case #%i:' % (t + 1), 'INSOMNIA')
        continue
    
    d = { str(i) : False for i in range(10) }
    toget = 10
    y = 0
    while toget > 0:
        y = y + N
        for c in str(y):            
            if not d[c]:
                toget = toget - 1
                d[c] = True        
    print('Case #%i:' % (t + 1), y)