T = int(input())

for t in range(1, T + 1):
    row = list(input()[::-1])
    res = 0
    while True:
        flag = False
        out = []
        # Handle beginning +
        while len(row) > 0 and row[-1] == '+':
            flag = True
            row.pop()
            out.append('-')
        # Handle all +
        if len(row) == 0:
            print('Case #{0}: {1}'.format(t, res))
            break
        if flag:
            res += 1
            row.extend(out)
        # Handle beginning -
        out = []
        flag = False
        while len(row) > 0 and row[-1] == '-':
            flag = True
            row.pop()
            out.append('+')
        if flag:
            res += 1
            row.extend(out)
