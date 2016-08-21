out = open('out.txt', 'w')
ca = 0
with open('D-small-attempt0.in') as f:
    for line in f:
        # print(line)
        if ca == 0:
            ca += 1
            continue
        s = int(line.strip().split()[2])
        out.write('Case #{}: {}\n'.format(ca, ' '.join(str(x+1) for x in range(s))))
        print('Case #{}: {}'.format(ca, ' '.join(str(x+1) for x in range(s))))
        ca += 1
