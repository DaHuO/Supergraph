file = open('A-large.in', 'r')
output = open('A-large.ou', 'w')

T = file.readline()
i = 1
for line in file:
    N = int(line)
    res = 'INSOMNIA'

    if N != 0:
        asleep = False
        digits = [False for _ in range(10)]

        j = 1
        number_str = ''
        while not(asleep):
            number = N * j
            number_str = str(number)

            for digit in number_str:
                digits[int(digit)] = True

            asleep = (digits == [True for _ in range(10)])
            j += 1

        res = number_str

    print('Case #' + str(i) + ': ' + res)
    output.write('Case #' + str(i) + ': ' + res + '\n')
    i += 1

output.close()




