def digit_list(num):
    return map(int, str(num))


def find_answer(num):
    if num == 0:
        return 'INSOMNIA'
    seen = set()
    current = 0
    while len(seen) < 10:
        current += num
        seen.update(digit_list(current))
    return current


if __name__ == '__main__':
    n = int(raw_input())
    test_cases = [int(raw_input()) for _ in range(n)]
    for i, tc in enumerate(test_cases):
        print 'Case #{}: {}'.format(i+1, find_answer(tc))