filename = 'B-large'

fi = open(filename+'.in', 'r')
fo = open(filename+'.out', 'w')
size = fi.readline()

for case, line in enumerate(fi, start=1):
    fo.write('Case #{}: '.format(case))
    pancakes = line.strip()
    pancakes = pancakes[::-1]
    pos = pancakes.find('-')
    n = 0
    if pos == -1:
        fo.write(str(n)+'\n')
        continue

    n = 1
    last = '-'

    for char in pancakes[pos:]:
        if char != last:
            n += 1
            last = char

    fo.write(str(n)+'\n')
