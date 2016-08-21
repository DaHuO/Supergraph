tests = int(raw_input())
for i in range(1, tests + 1):
    base = raw_input()
    if base == '0':
        print("Case #%i: INSOMNIA" % i)
        continue
    numbers = set(map(int, base))
    base_i = int(base)
    mult = 1
    while len(numbers) != 10:
        mult += 1
        n = mult * base_i
        numbers.update(set(map(int, str(n))))
    print("Case #%i: %i" % (i, n))
