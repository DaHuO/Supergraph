def calc_result(line):
    changes = 0
    for i, side in enumerate(line):
        try:
            if side != line[i + 1]:
                changes += 1
        except IndexError:
            if side == '-':
                return changes + 1
            else:
                return changes


if __name__ == '__main__':
    from sys import stdin

    is_header = False
    for case, line in enumerate(stdin.read().split()):
        if not is_header:
            is_header = True
            continue
        print('Case #{}: {}'.format(case, calc_result(line)))
