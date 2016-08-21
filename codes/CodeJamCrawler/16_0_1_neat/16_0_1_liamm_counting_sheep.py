def count_sheep(n, i=1, digits_seen = None):
    if not digits_seen:
        digits_seen = set()

    if n == 0:
        return 'INSOMNIA'

    m = n*i

    digits_seen.update(int(c) for c in str(m))

    if len(digits_seen) == 10:
        return m

    return count_sheep(n, i+1, digits_seen)


print(count_sheep(0) == 'INSOMNIA')
print(count_sheep(1) == 10)
print(count_sheep(2) == 90)
print(count_sheep(11) == 110)
print(count_sheep(1692) == 5076)

with open('A-large.in.txt') as f, open('A-large.out.txt', 'w') as g:
    n = int(f.readline())
    for case_num in range(1, n+1):
        inp = int(f.readline())
        ans = count_sheep(inp)
        g.write("Case #{}: {}\n".format(case_num, ans))
