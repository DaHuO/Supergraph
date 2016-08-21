import re
import time
import unittest

import math


class TestCoinJam(unittest.TestCase):
    def is_prime(self, n):
        if n == 2:
            return True, 0
        if n % 2 == 0 or n <= 1:
            return False, 2

        sqr = int(math.sqrt(n)) + 1

        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False, divisor
        return True, 0

    def get_number(self, inputstring):
        output = []
        for i in range(2, 11):
            value = int(inputstring, i)
            isprime, divisor = self.is_prime(value)
            if isprime:
                return None
            output.append(str(divisor))
        return ' '.join(output)

    def test_coinjam(self):
        linecount = 0
        input = ''
        with open('C:\Projects\googlecodejam\output.txt', 'w+') as output_file:
            output_file.truncate()
            with open('C:\Projects\googlecodejam\input.txt') as input_file:
                for line in input_file:
                    if linecount > 0:
                        length, repeat = line.split(' ')
                        repeat = int(repeat.strip())
                        output_file.write('Case #{0}:\n'.format(linecount))
                        for i in range(1, 1000000):
                            inputstring = '1' + '{0:b}'.format(i).rjust(int(length)-2, '0') + '1'
                            result = self.get_number(inputstring)
                            if result is not None:
                                output_file.write('{0} {1}\n'.format(inputstring, result))
                                repeat -= 1
                                if repeat == 0:
                                    break
                    linecount += 1