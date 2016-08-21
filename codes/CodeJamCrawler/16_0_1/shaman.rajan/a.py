
T = input()

for t in range(T):
    N = input()
    if N < 1:
        print "Case #%d: INSOMNIA" % (t+1)
        continue
    
    dig = [0] * 10
    num = 0
    while sum(dig) < 10:
        num += N
        temp = num
        while temp != 0:
            digit = temp % 10
            if dig[digit] == 0:
                dig[digit] = 1
            temp = temp/10

    print "Case #%d: %d" % ((t+1), num)
