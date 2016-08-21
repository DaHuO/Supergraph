t = int(raw_input())
for i in range(1,t+1):
    result = "INSOMNIA"
    b = set('1234567890')
    n = int(raw_input())
    if n!= 0:
        for j in range(1,100):
            newN = n*j
            a = set(str(newN))
            b = b.difference(a)
            if len(b) == 0:
                result = newN
                break
    print "Case #"+str(i)+": "+str(result)