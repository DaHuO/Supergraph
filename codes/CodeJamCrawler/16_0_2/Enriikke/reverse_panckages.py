input_file_name = './B-large.in'
output_file_name = './B-large-output.out'


def stacks(n):
    if n == ():
        return 0
    c = n[0]
    for i in xrange(1, len(n)):
        if n[i] != c:
            return 1 + stacks(n[i:])
    return 1

try:
    in_file = open(input_file_name)
    out_file = open(output_file_name, 'w')

    # Number of Cases
    N = in_file.readline()

    for n in range(int(N)):
        S = list(in_file.readline().strip())
        C = tuple([x == "+" for x in S])

        solution = stacks(C)
        if C[len(C) - 1]:
            solution -= 1

        out_file.write('Case #' + str(n + 1) + ': ' + str(solution) + '\n')

    # Done
    in_file.close()
    out_file.close()

except IOError as e:
    print 'File ' + input_file_name + ' not found.'
    print e.errno
    print e.strerror
