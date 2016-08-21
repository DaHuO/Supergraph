input=raw_input()
for casenumber in xrange(1,int(input)+1):
    asleep=False
    digits=["0","1","2","3","4","5","6","7","8","9"]
    t=0
    n=int(raw_input())
    while not asleep:
        t=t+1
        for digit in str(n*t):
            if digit in digits:
                digits.remove(digit)
                if not digits:
                    asleep=True
                    print "Case #"+str(casenumber)+": "+str(n*t)
        if t>1000000 and len(digits)!=0:
            asleep=True
            print "Case #"+str(casenumber)+": INSOMNIA"