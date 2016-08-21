import sys

firstline = True
n = 1
for line in sys.stdin:
    if firstline:
        firstline = False
    else:
        val = int(line)
        def digs(v):
            return [int(i) for i in list(str(v))]
        cur_val = 0
        cnts = [0 for i in range(10)]
        conv_time = -1

        while min(cnts) < 1 and conv_time < 10000:
            cur_val = cur_val + val
            dig_lst = digs(cur_val)
            for i in dig_lst:
                cnts[i] += 1
            conv_time += 1

        if min(cnts) < 1:
            print 'Case #' + str(n) + ': ' + 'INSOMNIA'
        else:
            print 'Case #' + str(n) + ': ' + str(cur_val)
        n += 1

