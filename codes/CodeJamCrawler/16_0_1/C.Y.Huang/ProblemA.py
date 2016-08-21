
def solve(num: int) -> int:
    has_shown = {}

    # run 1N ~ 10N
    m = -1
    last_num = -1
    while True:

        m += 1
        new_num = m * num
        if new_num == last_num:
            break
        else:
            last_num = new_num

        digits = get_digits(new_num)
        for d in digits:
            has_shown[d] = True

        if end_check(has_shown):
            return new_num
    return -1


def get_digits(num: int) -> []:
    digits = []
    while num:
        digits.append(num%10)
        num //= 10
    return list(set(digits))


def end_check(l: {}) -> bool:

    for d in range(10):
        if not l.get(d):
            return False

    return True

if __name__ == '__main__':

    lines_count = int(input())

    numbers = []
    for i in range(lines_count):
        numbers.append(int(input()))

    for idx, n in enumerate(numbers):
        result = solve(n)
        print('Case #%d: ' %(idx+1), end='')
        if result == -1:
            print('INSOMNIA')
        else:
            print('%d' %result)