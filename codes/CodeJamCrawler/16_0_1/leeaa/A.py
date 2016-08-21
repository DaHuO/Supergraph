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
    S = raw_input()

    ans = ""
    if len(S):
        for c in S:
            if len(ans) == 0 or ord(c)>=ord(ans[0]):
                ans = str(c) + ans
            else:
                ans += str(c)

    #print 'Case #' + str(ti) + ':'
    #for i in xrange(0, N):
    #    print ' '.join(map(str, mT[i]))
    print 'Case #' + str(ti) + ': ' + ans
