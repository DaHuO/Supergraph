def actualState(char, step):
    if (step % 2) == 0:
        return char
    else:
        if char == '+':
            return '-'
        else:
            return '+'

input = int(raw_input())

for case in range(1, input+1):
    line = raw_input()
    line = list(line)
    step = 0

    for x in reversed(line):
        act = actualState(x, step)
        if act == '-':
            step += 1
    print "Case #" + str(case) + ": " + str(step)
