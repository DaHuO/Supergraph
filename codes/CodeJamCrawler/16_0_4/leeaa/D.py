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
    K,C,S = map(int, raw_input().split())
    ans = []
    for i in xrange(1, K+1):
        tmp = i
        for j in xrange(1, C):
            tmp = (tmp - 1) * K + i
        ans.append(tmp)

    #print 'Case #' + str(ti) + ':'
    #for i in xrange(0, N):
    #    print ' '.join(map(str, mT[i]))
    print 'Case #' + str(ti) + ': ' + ' '.join(map(str,ans))
