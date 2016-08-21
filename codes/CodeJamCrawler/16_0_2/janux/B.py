def flip(group, i):
    for j in xrange(i):
        group[j] = ('-' if group[j] == '+' else '+')    
    
T = int(raw_input())

for case in xrange(1, T+1):    
    group = list(raw_input())
    N = len(group)
    manouvers = 0
    for i in xrange(N-1, -1, -1):       
        if group[i] != '+':
            flip(group, i)
            manouvers += 1
    print "Case #%s: %s" % (str(case), str(manouvers))
        
    

