from collections import Counter

def make_sort(new_cur):
    if len(new_cur) == 1:
        return new_cur
    middle = len(new_cur) // 2
    left = make_sort(new_cur[:middle])
    right = make_sort(new_cur[middle:])
    if left < right:
        return left + right
    else:
        return right + left

def count(N, R, P, S):
    answers = []
    for start in ['R', 'P', 'S']:
        cur = [start]
        while len(cur) != 2**N:
            new_cur = []
            for x in cur:
                if x == 'R':
                    new_cur += ['S', 'R']
                elif x == 'S':
                    new_cur += ['P', 'S']
                else:
                    new_cur += ['R', 'P']
            cur = new_cur
        if new_cur.count('R') == R and new_cur.count('P') == P and new_cur.count('S') == S:
            answers.append(''.join(make_sort(new_cur)))
    answers.sort()
    if len(answers) != 0:
        return answers[0]
    return 'IMPOSSIBLE'
with open('A-large.in', 'r') as f, open('a.out', 'w') as g:
    tests = None
    n = 0
    for line in f:
        line = line.rstrip()
        if tests is None:
            tests = int(line)
            continue
        n += 1
        N, R, P, S = map(int, line.split())
        ans = count(N, R, P, S)
        g.write('Case #' + str(n) + ': ' + ans + '\n')
