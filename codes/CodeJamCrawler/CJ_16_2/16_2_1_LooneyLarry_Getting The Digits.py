# Google Code Jam 2016 1BA
digits = [
[0, 'ZERO', 'Z'],
[2, 'TWO', 'W'],
[4, 'FOUR', 'U'],
[6, 'SIX', 'X'],
[8, 'EIGHT', 'G'],
[1, 'ONE', 'O'],
[3, 'THREE', 'H'],
[5, 'FIVE', 'F'],
[7, 'SEVEN', 'V'],
[9, 'NINE', 'N']]

def process(S, d, answer):
    digit, word, letter = d
    while S[letter] > 0:
        answer += [digit]
        for l in word:
            S[l] -= 1

def doCase(S, answer):
    for d in digits:
        process(S, d, answer)
    return ''.join(map(str, sorted(answer)))

cases = int(raw_input())
for i in range(cases):
    S = {}
    for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        S[l] = 0
    for l in raw_input().strip():
        S[l] += 1
    print 'Case #{}: {}'.format(i+1, doCase(S, []))
