import sys

T = int(sys.stdin.readline())

for i in range(1, T+1):
    line = str.strip(sys.stdin.readline())
    stack = []
    for a in line:
        if a == '+':
            stack.append(True)
        else:
            stack.append(False)

    # reduce
    last = stack[0]
    reduced = [last]
    for p in stack:
        if p == last:
            continue
        else:
            reduced.append(p)
            last = p

    if len(reduced) == 1:
        if stack[0]:
            print('Case #' + str(i) + ': 0')
        else:
            print('Case #' + str(i) + ': 1')
        continue

    if reduced[-1]:
        print('Case #' + str(i) + ': ' + str(len(reduced) - 1))
    else:
        print('Case #' + str(i) + ': ' + str(len(reduced)))
