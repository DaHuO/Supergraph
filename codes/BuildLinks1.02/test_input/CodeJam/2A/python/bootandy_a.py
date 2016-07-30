
import itertools

def winner(a, b):
    if a =='r' and b =='p':
        return b
    elif a =='r' and b =='s':
        return a
    elif a =='p' and b =='s':
        return b
    elif a =='p' and b =='r':
        return a
    elif a =='s' and b =='p':
        return a
    elif a =='s' and b =='r':
        return b
    return None

def run_game(chars):
    old_array = chars
    new_array = []
    while len(old_array) != 1:
        for i in range(0, len(old_array), 2):
            na = winner(old_array[i], old_array[i+1])
            if not na:
                return None
            else:
                new_array.append(na)
        old_array = new_array
        new_array = []

    return chars


def solve(r, p, s):
    pos = []
    for i in range(0, r):
        pos.append('r')
    for i in range(0, p):
        pos.append('p')
    for i in range(0, s):
        pos.append('s')
    options = list(itertools.permutations(pos, len(pos)))
    options.sort()
    #print(options)
    for o in options:
        if run_game(o):
            return ''.join(o)
    return 'IMPOSSIBLE'



#with open('A-sample.in') as f:
with open('A-small-attempt0.in') as f:
#with open('A-large-practice.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        words = f.readline().strip()
        n, r, p, s = map(int, words.split(' '))

        ans = solve(r, p, s)

        print('Case #%s: %s' % (str(puzzle_count + 1), ans.upper()))

