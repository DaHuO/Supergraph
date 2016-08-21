T = int(raw_input())
for t in range(1, T+1):
    map = {}
    N = int(raw_input())
    for n in range(0, 2*N-1):
        lst = raw_input().split(" ")
        for num in lst:
            if num not in map:
                map[num] = 0
            map[num] += 1
    rst = []
    for key in map:
        if map[key] % 2 == 1:
            rst.append(int(key))
    rst.sort()
    print "Case #" + str(t) + ": " + ' '.join(str(x) for x in rst)
