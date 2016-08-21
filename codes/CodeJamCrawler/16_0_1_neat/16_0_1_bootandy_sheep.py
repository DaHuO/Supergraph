

def to_char(n):
    chars = set()
    if n == 0:
        return set([0])
    while n:
        chars.add(n % 10)
        n = n // 10
    return chars

def solve(n):
    original_n = n
    all_chars = set([])
    #steps = []
    if n == 0:
        return 'INSOMNIA'

    while True:
        c = to_char(n)
        all_chars.update(c)
        if len(all_chars) == 10:
            return str(n)
        # if c in steps:
        #     return 'INSOMNIA'
        #steps.append(c)
        n = n + original_n

# print(to_char(10))
# print(to_char(1692))

#with open('sample.in') as f:
with open('A-large.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        i = f.readline().strip()
        ans = solve(int(i))
        print('Case #%s: %s' % (str(puzzle_count + 1), ans))
