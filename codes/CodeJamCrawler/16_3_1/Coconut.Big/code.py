T = int(raw_input().strip())
for t in xrange(T):
    N = int(raw_input().strip())
    senators = [int(i) for i in raw_input().strip().split()]

    in_senators = [0,] * N
    num_in = 0
    output = list()
    while sum(senators) > 0:
        i = 0
        while i < N:
            if senators[i] > 0:
                break
            i += 1

        selected = chr(65 + i)
        num_in += 1
        in_senators[i] += 1
        senators[i] -= 1
        if in_senators[i] > num_in / 2:
            j = 0
            while j < N:
                if senators[j] > 0 and i != j:
                    break
                j += 1
            selected += chr(65 + j)
            num_in += 1
            in_senators[j] += 1
            senators[j] -= 1
        output.append(selected)
    
    result = 'Case #%d: ' % (t + 1,)
    output.reverse()
    for s in output:
        result += '%s ' % (s,)
    print result
        
