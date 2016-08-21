def get_digits(n):
    return set([int(c) for c in str(n)])
all_digits = set(range(10))
def count_sheep(n):
    if n == 0:
        return 'INSOMNIA'
    else:
        i = 1
        new_n = i * n
        digits = get_digits(n)
        if digits == all_digits:
            return new_n
        while digits != all_digits:
            i += 1
            new_n = i * n
            digits = digits.union(get_digits(new_n))
        return new_n
f_stub = 'A-large'
f = open(f_stub + '.in', 'r')
o = open(f_stub + '.out', 'w')
n_cases = int(f.readline())
i = 0
while i < n_cases:
    n = int(f.readline())
    sheep_max = count_sheep(n)
    i += 1
    o.write('Case #' + str(i) + ': ' + str(sheep_max) + '\n')
f.close()
o.close()
