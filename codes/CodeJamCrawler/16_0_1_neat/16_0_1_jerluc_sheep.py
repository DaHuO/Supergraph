import fileinput


ALL_NUMBERS = set('0123456789')


def sleep_number(N):
    if N == 0:
        return 'INSOMNIA'
    i = 1
    seen = set()
    while True:
        case = N * i
        seen = set(str(case)) | seen
        if ALL_NUMBERS == seen:
            return case
        else:
            i += 1


if __name__ == '__main__':
    input = fileinput.input()
    T = int(input.readline())
    for i in range(0, T):
        case = int(input.readline())
        answer = sleep_number(case)
        print('Case #%d: %s' % (i+1, answer))
