# 2016-QR-A: Counting Sheep

import sys

def digits_in(num):
    if num == 0:
        yield 0
        return
    while num > 0:
        yield num % 10
        num = num / 10

def bleatrix(startnum):
    seen = {i: False for i in range(10)}
    num = startnum
    if num == 0:
        return 'INSOMNIA'
    while num < sys.maxint:
        for d in digits_in(num):
            seen[d] = True
        if all(seen.values()):
            return num
        num += startnum
    return 'INSOMNIA'

def main():
    num_cases = int(raw_input())
    for case_id in xrange(num_cases):
        start_num = int(raw_input())
        stop_num = bleatrix(start_num)
        print "Case #{0}: {1}".format(case_id + 1, stop_num)

main()
