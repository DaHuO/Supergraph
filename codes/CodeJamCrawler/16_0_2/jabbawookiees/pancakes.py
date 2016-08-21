
ss = None
memo = {}


def solve(length, happy):
    global ss
    if memo.get((length, happy), None) is not None:
        return memo[length, happy]

    if length == 1:
        if happy and ss[0] == '+':
            return 0
        elif not happy and ss[0] == '-':
            return 0
        else:
            return 1
    if happy:
        if ss[length - 1] == '+':
            answer = solve(length - 1, True)
        else:
            answer = solve(length - 1, False) + 1
    else:
        if ss[length - 1] == '-':
            answer = solve(length - 1, False)
        else:
            answer = solve(length - 1, True) + 1

    memo[length, happy] = answer
    return answer

cases = int(raw_input())

for ctr in xrange(cases):
    ss = raw_input()
    memo = {}
    answer = solve(len(ss), True)
    print "Case #%d: %d" % (ctr + 1, answer)
