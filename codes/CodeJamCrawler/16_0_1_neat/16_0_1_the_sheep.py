input_file = "A-large.in"
output_file = "outbla.txt"

with open(input_file) as in_file, open(output_file, 'w') as out_file:
    testcases = int(in_file.readline())
    for i in range(1, testcases + 1):
        n = int(in_file.readline())
        done = set()

        if n == 0:
            out_file.write('Case #{}: {}\n'.format(i, 'INSOMNIA'))
            continue

        for mult in range(1, 9999):
            last = mult
            done = done.union([int(x) for x in str(n * mult)])

            if len(done) == 10:
                break

        if len(done) == 10:
            out_file.write('Case #{}: {}\n'.format(i, last * n))
        else:
            out_file.write('Case #{}: {}\n'.format(i, 'INSOMNIA'))