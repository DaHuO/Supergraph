import sys

CONSTANTS = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN',
             'EIGHT', 'NINE']
result_list = []


def remove_word(S, word):
    N = min(S.count(i) for i in word)
    for i in range(N, -1, -1):
        if i == 0:
            yield (S, i)
        SS = S
        for j in word:
            SS = SS.replace(j, '', i)
        yield (SS, i)


def _get_digits(S, i):
    global result_list
    if i == 10:
        return False
    for S1, count in remove_word(S, CONSTANTS[i]):
        if not S1:
            result_list[i] = count
            return True
        if _get_digits(S1, i + 1):
            result_list[i] = count
            return True
    return False


def get_digits(S):
    global result_list
    result_list = [0] * 10
    _get_digits(S, 0)
    result = ''
    for i, count in enumerate(result_list):
        result += str(i) * count
    return result


lines = open(sys.argv[1]).readlines()[1:]
for i, S in enumerate(lines):
    result = get_digits(S.strip())
    print('Case #{}: {}'.format(i + 1, result))
