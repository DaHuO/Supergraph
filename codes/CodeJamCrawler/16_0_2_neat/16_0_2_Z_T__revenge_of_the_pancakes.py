def flip(stack, end):
    for index in xrange(end + 1):
        if stack[index] == '+':
            stack[index] = '-'
        else:
            stack[index] = '+'


for case_num in xrange(int(raw_input())):
    stack = list(raw_input())
    runner = len(stack) - 1
    count = 0

    while runner >= 0:
        if stack[runner] == '-':
            flip(stack, runner)
            count += 1
        runner -= 1

    print 'Case #{}: {}'.format(case_num + 1, count)
