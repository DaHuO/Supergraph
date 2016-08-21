from heapq import heappush, heappop

k = int(input())

for t in range(k):
    p = int(input())
    l = list(map(int, input().split(' ')))
    #print(l)
    maxs = 0
    s = sum(l)
    ans = 0
    #print(s)
    flag = False
    print("Case #%d:" % (t+1), end=" ")
    if s%2==1:
        for i in range(len(l)):
            if maxs < l[i]:
                ans = i
                maxs = l[i]
        l[ans] -= 1
        print(chr(ord('A')+ans), end ="")
        flag = True
        s -= 1
    h = []
    it = 0

    for item in l:
        if item != 0:
            heappush(h, (-item, chr(ord('A')+it)))
        it += 1
    #print(h)
   #print(h)
    while len(h) > 0:
        #print(h)
        #print("Sum:", s)
        for item in h:
            o = (-item[0])
            o = float(o/s)
            #print(item[1], o)
            #if o > 0.5:
            #    print("FAIL")
        p = heappop(h)
        r = heappop(h)
        p_tmp = (p[0]+1, p[1])
        r_tmp = (r[0]+1, r[1])
        if flag:
            print("", p[1], end="")
        else:
            print(p[1], end="")
        flag = True
        print(r[1], end="")
        if p_tmp[0] < 0:
            heappush(h, p_tmp)
        if r_tmp[0] < 0:
            heappush(h, r_tmp)
        s -=2


    print()

