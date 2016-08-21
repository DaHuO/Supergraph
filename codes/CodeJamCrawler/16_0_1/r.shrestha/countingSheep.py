import sys


with open(sys.argv[1]) as f:
    content = f.read().splitlines()

T = int(content[0])

with open('io/sheep.out', 'w') as f:
    for caseIndex in xrange(1, T+1):
        N = int(content[caseIndex])
        if N == 0:
            f.write('Case #%d: %s\n' % (caseIndex, 'INSOMNIA'))
            print 'Case #%d: %s, %d' % (caseIndex, 'INSOMNIA', N)
        else:
            unseenDigits = {i:True for i in range(10)}
            i = 1
            while len(unseenDigits):
                lastNumber = i * N
                temp = lastNumber
                while temp:
                    digit = temp % 10
                    temp = temp / 10
                    if digit in unseenDigits:
                        del unseenDigits[digit]
                i += 1

                # debug
                # print "case #%d: %d" % (caseIndex, lastNumber)
                # print unseenDigits, '\n'

            f.write('Case #%d: %d\n' % (caseIndex, lastNumber))
            print 'Case #%d: %d, %d' % (caseIndex, lastNumber, N)


    

