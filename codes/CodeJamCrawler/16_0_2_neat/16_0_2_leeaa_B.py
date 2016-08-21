tn = int(raw_input())
# left is basic
# up 270
# right 180
# down 90

def reverseT(Arr, right):
    for i in xrange(0, right+1):
        Arr[i] *= (-1)
    left = 0
    while right > left:
        Arr[left], Arr[right] = Arr[right], Arr[left]
        right -= 1
        left += 1

for ti in xrange(1, tn+1):
    D = raw_input()
    data = []
    for c in D:
        if c == '-':
            data.append(-1)
        else:
            data.append(1)
    bot = len(data)-1
    ans = 0
    while bot >= 0:
        while bot >=0 and data[bot] == 1:
            bot -= 1
        if bot >= 0:
            if data[0] == 1:
                top = 0
                while top <= bot and data[top] == 1:
                    top += 1
                reverseT(data,top-1)
                ans += 1
            if data[bot] == -1:
                reverseT(data, bot)
                ans += 1

    #print 'Case #' + str(ti) + ':'
    #for i in xrange(0, N):
    #    print ' '.join(map(str, mT[i]))
    print 'Case #' + str(ti) + ': ' + str(ans)
