tn = int(raw_input())
# left is basic
# up 270
# right 180
# down 90

def check(Arr, number):
    while number > 0:
        Arr[number%10] = 1
        number /= 10

for ti in xrange(1, tn+1):
    N = int(raw_input())
    ans_str = ""
    if N == 0:
        ans_str = "INSOMNIA"
    else:
        originalN = N
        T = [0 for i in range(10)]
        while N%10 == 0:
            N /= 10
            T[0] = 1
        ans = 0
        while sum(T) != 10:
            ans += 1
            if ans % 10 == 0:
                T[0] = 1
                continue
            check(T, N*ans)
        ans_str = str(originalN*ans)


    #print 'Case #' + str(ti) + ':'
    #for i in xrange(0, N):
    #    print ' '.join(map(str, mT[i]))
    print 'Case #' + str(ti) + ': ' + ans_str
