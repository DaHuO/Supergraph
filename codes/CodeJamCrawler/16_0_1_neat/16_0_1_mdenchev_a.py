fin = open('a.in', 'r')
fout = open('a.out', 'w')

no_cases = fin.readline()

cases = map(int, fin.readlines())

for i, case in enumerate(cases):
    if case == 0:
        fout.write('Case #' + str(i+1) + ': INSOMNIA\n')
    else:
        count = 0
        seen = set()
        while len(seen) != 10:
            count += 1
            num = case * count
            for ch in str(num):
                seen.add(ch)
        fout.write('Case #' + str(i+1) + ': ' + str(num) + '\n')
