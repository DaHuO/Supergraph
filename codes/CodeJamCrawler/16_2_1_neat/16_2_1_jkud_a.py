#!/usr/bin/env python


words = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
chars_list = [
    {'Z': 0, 'W': 2, 'U': 4, 'X': 6, 'G': 8},
    {'O': 1, 'R': 3, 'S': 7},
    {'F': 5, 'N': 9}
]


def remove(wd, letters):
    for letter in letters:
        wd[letter] -= 1
        if wd[letter] == 0:
            del wd[letter]
    return wd


def solve(word):
    num = []
    wd = {}
    for l in word:
        if l in wd:
            wd[l] += 1
        else:
            wd[l] = 1
    for chars in chars_list:
        for (c, d) in chars.items():
            while c in wd:
                num.append(d)
                wd = remove(wd, words[d])
    return ''.join(str(d) for d in sorted(num))


T = int(raw_input().strip())
for t in range(T):
    word = raw_input().strip()
    print 'Case #%d: %s' % (t+1, solve(word))
