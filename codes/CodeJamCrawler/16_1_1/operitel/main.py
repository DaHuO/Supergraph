file = open('A-large.in', 'r')
output = open('A-large.ou', 'w')

T = int(file.readline().rstrip())
i = 1
for line in file:
    line = line.rstrip()

    res = ''

    for chr in line:
        if len(res) == 0:
            res += chr
        elif chr >= res[0]:
            res = chr + res
        else:
            res = res + chr

    print('Case #' + str(i) + ': ' + str(res))
    output.write('Case #' + str(i) + ': ' + str(res) + '\n')
    i += 1

output.close()