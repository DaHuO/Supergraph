#!/usr/bin/env python


with open("x") as f:
    array = [int(x) for line in f for x in line.split()]

a = array[4]


with open("fw", 'w') as f:
    for test in range(1, len(array)):

        num = array[test]
        f.write("Case #" + str(test) + ": ")
        tab = {}
        x = 0
        for i in range(1, 10000001):
            if i == 10000000:
                f.write('INSOMNIA\n')
            x = x + num

            tmp = x
            while tmp > 0:
                tab[tmp % 10] = 1
                tmp /= 10

            if len(tab) == 10:
                f.write(str(x)+'\n')
                break