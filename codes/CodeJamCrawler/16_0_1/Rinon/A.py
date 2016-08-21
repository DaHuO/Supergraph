import sys

with open(sys.argv[1], 'r') as f:
    f.readline()
    case = 0
    for line in f:
        case += 1
        n = int(line)
        if n == 0:
            print('Case #{}: INSOMNIA'.format(case))
            continue

        x = 0
        found = 0
        while found != 0x3ff:
            x += n
            for c in str(x):
                found |= (1 << (ord(c)-ord('0')))

        print('Case #{}: {}'.format(case, x))
