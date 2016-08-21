#!/usr/bin/python
lines = [int(x) for x in open("large_input.in", 'rt').readlines()]

for i in range(1, lines[0]+1):
    N = lines[i]
    result = None
    visited = [False] * 10
    for n in range(1, 100000):
        num = str(n * N)
        #print "num:", num
        for t in range(len(num)):
            visited[int(num[t])] = True
        check = True 
        for k in range(len(visited)):
            check = check and visited[k]
        if check == True:
            result = num
            break
    print "Case #%d:" % i,
    if result is not None:
        print num
    else:
        print 'INSOMNIA'
