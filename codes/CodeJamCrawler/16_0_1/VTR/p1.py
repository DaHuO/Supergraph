__author__ = 'VTR'
import sys

assert(len(sys.argv) > 1)


def last_number(num):
    if num == 0:
        return 'INSOMNIA'
    freq = [0] * 10
    more_digs = 10
    sum_num = 0
    while more_digs > 0:
        sum_num += num
        s_num = str(sum_num)
        for c in s_num:
            idx = ord(c) - 48
            if freq[idx] > 0:
                continue
            else:
                freq[idx] = 1
                more_digs -= 1
    return sum_num


with open(sys.argv[1], 'r') as fp:
    t = int(fp.readline())
    for i in range(1, t+1):
        n = int(fp.readline())
        print 'Case #'+str(i)+': ' + str(last_number(n))