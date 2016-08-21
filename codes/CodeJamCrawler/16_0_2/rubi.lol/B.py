from collections import deque


def flip(test, index=0):
    part_a = test[index::-1]
    part_a = part_a.replace('+', '%temp%').replace('-', '+').replace('%temp%', '-')
    part_b = test[index+1::]
    return part_a + part_b


def solve(test):
    count = 0

    while True:
        last_s = test.rfind('-')
        if last_s < 1:
            return count + last_s + 1

        test = test[:last_s + 1]

        last_h = test.rfind('+')
        if last_h < 0:
            return count + 1

        if test[0] == '+':
            test = flip(test, last_h)
        else:
            test = flip(test, last_s)

        count = count + 1


T = int(raw_input())

for X in xrange(1, T + 1):
    S = raw_input()
    answer = solve(S)
    print "Case #{}: {}".format(X, answer)


