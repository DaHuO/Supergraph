from itertools import product

input=raw_input()
for casenumber in xrange(1,int(input)+1):
    n=raw_input().split()
    k=int(n[0])
    c=int(n[1])
    s=int(n[2])
    if s<k and c==1:
        print "Case #"+str(casenumber)+": IMPOSSIBLE"
    elif k==1:
        print "Case #"+str(casenumber)+": 1"
    elif s==k:
        section=k**c
        #print section
        check=[str(i+1) for i in range(0,section,section/k)]
        print "Case #"+str(casenumber)+": "+" ".join(check)
    else:
        possible=[list(i) for i in product("LG",repeat=k)]
        ways=[]
        for i in possible:
            save="".join(i)
            l=1
            original=save
            frontier=original
            while l<c:
                frontier=""
                for p in original:
                    if p=="L":
                        frontier+=save
                    else:
                        frontier+="G"*k
                original=frontier
                l+=1
            ways.append(frontier)
            #print "frontier",frontier,len(frontier)
        num=[0]*len(frontier)
        for i in xrange(0,len(ways)):
            for j in xrange(0,len(frontier)):
                if ways[i][j]=="L":
                    num[j]+=1
        if min(num)>s:
            print "Case #"+str(casenumber)+": IMPOSSIBLE"
        else:
            check=[]
            for i in xrange(0,len(num)):
                if num[i]<=s:
                    check.append(str(i+1))
                if len(check)==s:
                    break
            print "Case #"+str(casenumber)+": "+" ".join(check)