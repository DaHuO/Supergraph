num_problems = int(raw_input())

WORDS = [
    ('Z', "ZERO", 0), ('W', "TWO", 2), ('X', "SIX", 6), ('G', "EIGHT", 8),
    ('S', "SEVEN", 7),
    ('V', "FIVE", 5),
    ('I', "NINE", 9),
    ('N', "ONE", 1),
    ('F', "FOUR", 4),
    ('R', "THREE", 3),
]


def solve(s):
    nums = ''
    idx = 0
    while idx < 10:
        REQ_CHARS, CHARS, num = WORDS[idx]
        has_word = True
        for c in REQ_CHARS:
            if c not in s:
                has_word = False
                break

        if has_word:
            nums += str(num)
            for c in CHARS:
                s = s.replace(c, '', 1)
        else:
            idx += 1

    num_list = list(nums)
    num_list.sort()
    return ''.join(num_list)


for x in range(num_problems):
    s = str(raw_input())
    soln = solve(s)
    print 'Case #{}: {}'.format(x + 1, soln)
