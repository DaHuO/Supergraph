__author__ = 'Pavel'

file_name_read = 'A-large.in'
file_name_write = 'A-large.out'


class CountingSheep:

    def __init__(self):
        self.fr = open(file_name_read)
        self.fw = open(file_name_write, 'w')

    def read_cases(self):
        t = self.fr.readline()
        return t

    def read_each_case(self):
        for _ in xrange(int(self.read_cases())):
            yield self.fr.readline()

    def write_output(self, output, case_num):
        self.fw.write("Case #%d: " % case_num)
        self.fw.write(output)
        self.fw.write('\n')


def return_digits(number):
    return [int(i) for i in str(number)]

if __name__ == "__main__":
    cs = CountingSheep()
    case_num = 0
    for x in cs.read_each_case():
        case_num += 1
        x = x.replace('\n', '')
        x = int(x)

        if x == 0:
            cs.write_output('INSOMNIA', case_num)
            continue

        digits = set(range(0, 10))
        for i in xrange(1, 1000000):
            t = x * i
            digits -= set(return_digits(t))
            if len(digits) == 0:
                cs.write_output(str(t), case_num)
                break
        if i >= 1000000 - 1:
            cs.write_output('INSOMNIA', case_num)






