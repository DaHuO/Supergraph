T = input()

for k in range(T):
    
    N = input()

    heights = [0]*3000
    
    for i in range(2*N-1):
        tmp = raw_input()
        tmp = tmp.split(' ')
        for o in range(N):
            heights[int(tmp[o])] +=1

    l = []
    for i in range(3000):
        if heights[i]%2 == 1:
            l.append(i)
    s = ""
    for o in range(N):
        s = s+" " + str(l[o])
    print "Case #%d:"%(k+1)+s
