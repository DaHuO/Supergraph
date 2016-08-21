t = int(raw_input())
for tt in xrange(t) :
    print "Case #" + str(tt+1) + ":",
    n = int(raw_input())
    ##n = tt
    if n == 0 :
        print "INSOMNIA"
    else :
        digits = [0,1,2,3,4,5,6,7,8,9]
        i = 2
        j = n
        while i < 100000 :
            for each in str(n) :
                try :
                    #print each,
                    digits.remove(int(each))
                except :
                    x = 1
            ##print n
            if len(digits) == 0 :
                print n
                break
            else :
                n = i * j
                i += 1