t= int(raw_input())

for i in range(t):
    k  = int(raw_input())#N*N N
    l = []
    for j in range(2*k-1):
        l1 = map(int, raw_input().split())
        
        
        if len(l1) != '\n':
            l.append(l1)
    dic = {}
    for alist in l:
        for elt in alist:
            if elt not in dic:
                dic[elt] = 1
            else:
                dic[elt] = dic[elt] + 1
    final = []
    for elt in dic:
        if dic[elt] % 2 != 0:
            final.append(elt)
    final.sort()
    print "Case #"+str(i+1)+": ",
    for elt in final:print elt,
    print
        
            
        
