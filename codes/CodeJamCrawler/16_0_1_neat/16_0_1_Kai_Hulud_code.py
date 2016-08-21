tT = int(raw_input())
for Tcase in range(1,tT+1):
    sleep = False
    known = [];
    i = 0
    kMAX = 10
    N = int(raw_input())
    while(not(sleep)):
        if (N*i==N*(i+1)):
            break
        i+=1
        nMAX=i*N
        for num in str(nMAX):
            nom=int(num)
            if known.count(nom)<1:
                known.append(nom)
        if len(known)==kMAX:
            iN=i*N
            sleep = True
    if not(sleep):
        iN="INSOMNIA"
    print("Case #%s: %s" % (Tcase, iN))
