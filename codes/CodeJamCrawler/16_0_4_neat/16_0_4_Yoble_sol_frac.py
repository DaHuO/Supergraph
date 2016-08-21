with open('D-small-attempt1.in') as inp, open('output.out', 'w') as out:
    index = -1
    for line in inp:
        index += 1
        if index == 0: continue

        line = line.strip()
        k = int(line.split()[0])
        c = int(line.split()[1])
        s = int(line.split()[2])

        if s != k:
            print('case %i not small input' % index)

        tile_list = list()
        for i in range(k):
            if c > 2:
                tile_list.append(str(i*(k**(c-1)) + i*(k**(c-2)) + i+1))
            elif c == 2:
                tile_list.append(str(i*(k**(c-1)) + i+1))
            else:
                tile_list.append(str(i+1))


        out.write('Case #%i: ' % index + ' '.join(tile_list) + '\n')
