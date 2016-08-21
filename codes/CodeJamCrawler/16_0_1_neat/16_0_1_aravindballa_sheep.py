import sys

with open(sys.argv[1], 'r') as f:

    fout = open(sys.argv[2], 'w')

    T = f.readline().strip('\n')

    for t in range(int(T)):
        digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
        number = f.readline().strip('\n')

        if int(number) == 0:
            fout.write('Case #'+ str(t+1) +': INSOMNIA' + '\n')
            continue

        a = number
        i = 0

        while digits:
            i += 1
            a = str(int(number) * i)
            digits -= set(a)

        fout.write("Case #" + str(t+1) + ': ' + a + '\n')

    fout.close()