#use ipython

ap = []
cnt = 0
print("Case #1:")
for j in range(2147483649,4294967295,2):
    n2 = format (j,'b')
    ap = []
    ak = [0,0,0,0,0,0,0,0,0]
    flg = 0
    for i in range(2,11):
        kite = int(n2,i)

        ap.append(kite)

        ak[i - 2] = 0
        for k in [2,3,5,7,9]:
            if kite % k == 0:
                ak[i - 2]=str(k)
                break
        if ak[i - 2] != 0:
            flg = 1
        else:
            flg = 0
            break
   
    if flg == 1:
        flg = 0
        print(n2,' '.join(ak))
        cnt+=1
        if cnt > 499 :
            break
print(cnt)
