

T = int(raw_input())
for t in range(1,T+1):
    ulaz = raw_input().split()
    K,C,S = int(ulaz[0]),int(ulaz[1]),int(ulaz[2])
    print "Case #"+str(t)+": "+" ".join(str(e) for e in range(1,S+1))
