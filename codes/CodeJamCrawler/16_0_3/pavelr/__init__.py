import math
from random import randint
from itertools import count, islice
__author__ = 'Pavel'

file_name_read = 'a_small.in'
file_name_write = 'a_small.out'


class FileManager:

    def __init__(self):
        self.fr = open(file_name_read)
        self.fw = open(file_name_write, 'w')

    def _read_cases(self):
        t = self.fr.readline()
        return t

    def read_each_case(self):
        for _ in xrange(int(self._read_cases())):
            yield self.fr.readline().replace('\n', '')

    def write_output(self, output):
        self.fw.write(str(output))
        self.fw.write('\n')

    def print_case(self):
        self.fw.write("Case #%d:\n" % 1)

def random_jamcoin(len):
    return '1' + ''.join([str(randint(0, 1)) for _ in range(len - 2)]) + '1'


def binary_interp(num, base):
    new_num = 0
    power = len(num) - 1
    for ch in num:
        if int(ch) == 1:
            new_num += math.pow(base, power)
        power -= 1

    return new_num


def is_prime(n):
    for i in range(2, int(math.sqrt(n)-1)):
        if n % i == 0:
            return False, i
    return True, 0

def is_coinjam(num):
    div_list = []
    for base in range(2, 11):
        x = binary_interp(num, base)
        prime, div = is_prime(x)
        if prime:
            return False, []
        else:
            div_list.append(str(div))
    return True, div_list

if __name__ == "__main__":
    f = FileManager()
    count = 0
    output = ''
    f.print_case()
    returned_nums = []
    for case in f.read_each_case():
        length, j = case.split(' ')
        while count != int(j):
            num = random_jamcoin(int(length))
            coinjam, div_list = is_coinjam(num)
            print 'Number {0} is coinjam? {1}'.format(num, coinjam)
            if coinjam:
                if num not in returned_nums:
                    returned_nums.append(num)
                    msg = '{0} {1}'.format(num, ' '.join(div_list))
                    f.write_output(msg)
                    count += 1
                    print 'Current count is: {0}'.format(count)


