def getMinK(n):
    digits = range(0, 10)
    k = 1
    number = n
    while len(digits) > 0:
        sNumber = str(number)
#        print "povodne: %d nasobok:%d"%(n, number)
        for sdigit in sNumber:
            try:
                digits.remove(int(sdigit))
            except:
                pass
        k += 1
        number += n
    return number - n

t = int(raw_input())
for case in range(1, t+1):
    n = int(raw_input())
    if n == 0:
        print "Case #%d: INSOMNIA" % case
    else:
        print "Case #%d: %d" % (case, getMinK(n))


