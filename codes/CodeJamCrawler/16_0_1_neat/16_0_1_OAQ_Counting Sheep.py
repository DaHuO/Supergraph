f = open('A-large.in', 'r')
output = open('A-large.txt', 'w')

sheep = []
number = int(f.readline())

i = 0
while number > i:
    i += 1
    sheep.append(int(f.readline().strip('\n')))

i = 0
for sheep in sheep:
    i += 1
    N = 0
    num = []

    while True:
        N += 1
        s = str(sheep*N)
        for digit in s:
            if digit not in num:
                num.append(digit)
        if len(num) == 10:
            output.writelines('Case #%i: %d\n' % (i, sheep*N))
            break
        if N > 1000:
            output.writelines('Case #%i: %s\n' % (i, 'INSOMNIA'))
            break
