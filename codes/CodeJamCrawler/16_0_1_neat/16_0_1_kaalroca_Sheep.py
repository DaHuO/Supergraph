# -*- coding: utf-8 -*-

__author__ = 'kaalroca'


def sheep(n):
    i = 1

    if n == '0':
        return 'INSOMNIA'
    else:
        numbers = map(str, range(10))
        while True:
            result = int(n)*i
            i += 1
            for element in str(result):
                if element in numbers:
                    numbers.remove(element)

            if len(numbers) == 0:
                return result

t = int(raw_input())
for i in range(1, t + 1):
    num = raw_input()
    print "Case #{}: {}".format(i, sheep(num))

