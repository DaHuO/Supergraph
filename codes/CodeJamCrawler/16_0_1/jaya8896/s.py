st = "INSOMNIA"
for cases in range(input()):
    n = input()
    i = n
    if n==0:
        answer = st
    else:
        Covered_Digits = {}
        flag = 1
        while 1:
            st = str(n)
            for it in st:
                Covered_Digits[it] = 1
            if len(Covered_Digits)==10:
                fl = 0
                answer = n
                break
            n += i
        if fl==1:
            pass
    print "Case #"+ str(cases+1) + ": " + str(answer)
