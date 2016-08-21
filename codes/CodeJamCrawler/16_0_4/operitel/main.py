file = open('D-small-attempt0.in', 'r')
output = open('D-small-attempt0.ou', 'w')

T = int(file.readline().rstrip())
i = 1
for line in file:
    line = line.rstrip()

    K = int(line.split(' ')[0])
    C = int(line.split(' ')[1])
    S = int(line.split(' ')[2])

    res = ''
    if K == S:
        for j in range(1, S + 1):
            res += str(j) + ' '
        res = res[:-1]
    else:
        res = 'IMPOSSIBLE'

    print('Case #' + str(i) + ': ' + str(res))
    output.write('Case #' + str(i) + ': ' + str(res) + '\n')
    i += 1

output.close()