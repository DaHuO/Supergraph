f = open("input.txt","r+")
w = open("output.txt","w")
t = int(f.readline())
for a0 in range(1,t+1):
    n = int(f.readline())
    p = map(int,f.readline().split())
    res = []
    while(max(p) != 1):
        m = max(p)
        st = ''
        flag = 0
        if p.count(m)>1:
            for i in range (0,len(p)):
                if p[i] == m and flag < 2:
                    st += chr(97 + i)
                    flag+= 1
                    p[i] -= 1
            res.append(st)
            print a0,st
        else :
            inx = p.index(m)
            p[inx] -= 2
            st = chr(97 + inx) + chr(97 + inx)
            print a0,st
            res.append(st)
    while(max(p) == 1):
        m = 1
        cn = p.count(m)
        st = ''
        if (cn%2 == 1):
            for i in range (0,len(p)):
                if p[i] == 1:
                    st = chr(97+i)
                    p[i]-= 1
                    print a0,st
                    res.append(st)
                    break
        #print "-----",a0,st
        flag = 0
        st = ''
        for i in range(0,len(p)):
            if p[i] == 1 and flag <2:
                st += chr (97+i)
                p[i] -= 1
            if len(st)== 2:
                print "hello"
                flag = 0
                print a0,"-----",st
                res.append(st)
                st = ''
            #print a0,st
    ans = ''
    for i in range(0,len(res)):
        ans += res[i] + ' '
    print ans
    st = "Case #%d: "%a0 + ans
    print st
    w.write(st + "\n")




















    
f.close()
w.close()
