def pancake(cakes):
    count = 0
    flip = {'-': '+', '+': '-'}
    side = '+'
    for cake in reversed(cakes):
        if cake != side:
            count += 1
            side = flip[side]
    return count

if __name__ == '__main__':
    with open('B-large.in') as fin, open('output', 'w') as fout:
        fin.readline()
        for i, line in enumerate(fin, 1):
            fout.write('Case #%d: %d\n' % (
                i, pancake(line.strip())
            ))
