

T = int(raw_input())
for t in xrange(1, T+1):
    N = int(raw_input())
    current_set = set()
    for i in xrange(1, 101):
        x = i * N
        current_set |= set(str(x))
        if len(current_set) == 10:
            break
    if len(current_set) == 10:
        print('Case #%d: %d' %(t, x))
    else:
        print('Case #%d: INSOMNIA' %(t))





        


