input_file = "D-small-attempt0.in"
output_file = "outbla.txt"

with open(input_file) as in_file, open(output_file, 'w') as out_file:
    testcases = int(in_file.readline())
    for i in range(1, testcases + 1):
        help = in_file.readline().split()

        K = int(help[0])
        C = int(help[1])
        S = int(help[2])

        out_file.write('Case #{}: {}\n'.format(i, ' '.join([str(x) for x in range(1, S + 1)])))
