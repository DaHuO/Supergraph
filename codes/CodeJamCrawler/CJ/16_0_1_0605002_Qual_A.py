with open('A-small-attempt0.in', 'rb') as fin, open('out.txt', 'wb') as fout:
    n = int(fin.readline().strip())

    for cs in range(1, n + 1):
        p = int(fin.readline().strip())

        if p == 0:
            fout.write('Case #{}: INSOMNIA\n'.format(cs))
            continue
        q = 0
        dig = set()
        while(len(dig) < 10):
            q += p
            dig = dig.union([d for d in str(q)])
        fout.write('Case #{}: {}\n'.format(cs, q))
                   
