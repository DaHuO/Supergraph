import math

T = int(raw_input().strip())
for t in xrange(T):
    B, M = [int(i) for i in raw_input().strip().split()]
    if math.log(M, 2) > B - 2:
        print 'Case #%d: IMPOSSIBLE' % (t + 1,)
    else:
        print 'Case #%d: POSSIBLE' % (t + 1,)
        M -= 1
        result = [1,]
        for i in xrange(B - 2):
            result.append(M % 2)
            M /= 2
        result.append(0)
        result.reverse()
        output = ''
        for i in result:
            output += str(i)
        print output
        for row in xrange(B - 2):
            output = ''
            for col in xrange(B):
                if col <= row + 1:
                    output += '0'
                else:
                    output += '1'
            print output
        print '0' * B

