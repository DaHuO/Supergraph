T = int(input())
cake = [str(input()) for i in range(T)]
revenge = 0

for casenum in range(T):
    cakesize = len(cake[casenum])

    while(True):
        if "-" in cake[casenum]:
            revenge = revenge + 1
            rp = cake[casenum].rfind("-") + 1 #反転させる位置
            cake[casenum] = cake[casenum][0:rp].replace("-","A").replace("+","-").replace("A","+")
        else:
            print("Case #"+str(casenum+1)+": "+ str(revenge))
            revenge = 0
            break
