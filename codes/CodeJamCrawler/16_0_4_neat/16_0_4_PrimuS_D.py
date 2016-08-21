input_file = open('D-small-attempt0.in', 'r')
out_file = open('D-res.out', 'w')

test_cases = int(input_file.readline())

for t in range(1, test_cases + 1):
    k,c,s = (int(x) for x in input_file.readline().split())

    out_file.write('Case #{:d}:'.format(t))

    res = range(1, k + 1)
    res = [1 + (x-1) * k ** (c-1) for x in res]
    for x in res:
        out_file.write(' {:d}'.format(x))

    out_file.write('\n')