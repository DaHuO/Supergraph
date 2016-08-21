
def calc_result(line):
    result = abs(int(line))
    if result == 0:
        return "INSOMNIA"

    digits = set()
    while len(digits) < 10:
        for d in str(result):
            digits.add(d)
        if len(digits) == 10:
            return result
        result += int(line)

if __name__ == '__main__':
    from sys import stdin

    is_header = False
    for case, line in enumerate(stdin.read().split()):
        if not is_header:
            is_header = True
            continue
        print('Case #{}: {}'.format(case, calc_result(line)))
