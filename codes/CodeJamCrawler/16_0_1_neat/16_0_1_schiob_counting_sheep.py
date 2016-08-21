with open('A-small-attempt0.in', 'r') as f:
    t = int(f.readline())
    with open('A-small-attempt0.out', 'w') as outf:
        for i, row in enumerate(f, start=1):
            n = int(row)
            mult = 2
            seen = set(str(n))
            if n == 0:
                res = 'INSOMNIA'
            else:
                while len(seen) < 10:
                    val = n*mult
                    seen.update(str(val))
                    mult += 1
                res = val
            outf.write('Case #{}: {}\n'.format(i, res))