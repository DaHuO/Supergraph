input_file = "B-large.in"
output_file = "outbla.txt"

with open(input_file) as in_file, open(output_file, 'w') as out_file:
    testcases = int(in_file.readline())
    for i in range(1, testcases + 1):
        p = in_file.readline().rstrip('\n')
        count = 0

        cur = p[0]

        for j in range(0, len(p)):
            if cur != p[j]:
                count += 1
                cur = p[j]

        if cur == '-':
            count += 1

        out_file.write('Case #{}: {}\n'.format(i, count))
