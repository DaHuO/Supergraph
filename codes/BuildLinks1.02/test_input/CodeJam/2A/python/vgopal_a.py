from itertools import permutations

FILENAME = 'a-small.txt'

f = open(FILENAME)

def play_game(string):
    if len(string) == 1:
        return True
    winners = []
    for i in xrange(0, len(string), 2):
        letters = sorted([string[i], string[i+1]])
        if string[i] == string[i + 1]:
            return False
        elif letters == ['R', 'S']:
            winners.append('R')
        elif letters == ['P', 'R']:
            winners.append('P')
        else:
            winners.append('S')
    return play_game(''.join(winners))


def answer(N, R, P, S):
    string = 'R' * R + 'P' * P + 'S' * S
    works = None
    for permutation in permutations(string):
        permutation = ''.join(permutation)
        if play_game(permutation):
            if works is None or permutation < works:
                works = permutation
    if works:
        return works
    return 'IMPOSSIBLE'


num_cases = int(f.readline())
for case in xrange(1, num_cases + 1):
    N, R, P, S = [int(x) for x in f.readline().split()]
    val = answer(N, R, P, S)
    print 'Case #{}: {}'.format(case, val)
