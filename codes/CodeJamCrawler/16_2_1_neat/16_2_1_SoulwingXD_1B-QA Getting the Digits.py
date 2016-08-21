num_tests = int(input())

groups = list(zip('0246785139', ('ZERO', 'TWO', 'FOUR', 'SIX', 'SEVEN', 'EIGHT',\
                            'FIVE', 'ONE', 'THREE', 'NINE'), 'ZWUXSGFOTI'))

for n in range(num_tests):
    s = input()
    result = ''

    for num, num_s, l in groups:
        num_l = s.count(l)
        result += num*num_l
        for r in num_s:
            s = s.replace(r, '', num_l)

    result = ''.join(sorted(result))
    print("Case #{}: {}".format(n + 1, result))
