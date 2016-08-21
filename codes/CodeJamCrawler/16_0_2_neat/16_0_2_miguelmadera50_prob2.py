from itertools import groupby


def solution(number):
    number = [x[0] for x in list(groupby(number))]
    if number[-1] is '+':
        number = number[:-1]
    return len(number)


t = int(raw_input())
for i in range(1, t + 1):
    num = raw_input()
    print "Case #{0}: {1}".format(i, solution(num))