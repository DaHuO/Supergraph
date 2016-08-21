__author__ = 'Pavel'

file_name_read = 'B-large.in'
file_name_write = 'B-large.out'


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

    def write_output(self, output, case_num):
        self.fw.write("Case #%d: " % case_num)
        self.fw.write(str(output))
        self.fw.write('\n')


def check_list(lst):
    for elem in lst:
        if elem == '-':
            return False
    return True

def flip_all_next_to_opposite(str, sign, op_sign):
    flipped = False
    for ch in str:
        if ch == sign:
            str = str.replace(ch, op_sign, 1)
            flipped = True
        else:
            break

    return str, flipped


if __name__ == "__main__":
    f = FileManager()
    case_num = 0
    for x in f.read_each_case():
        case_num += 1
        count = 0
        occur_to_flip = 0

        if check_list(x):
            f.write_output(count, case_num)
            continue
        else:
            while not check_list(x):
                x, flipped = flip_all_next_to_opposite(x, '-', '+')
                if flipped:
                    count += 1
                else:
                    x, flipped = flip_all_next_to_opposite(x, '+', '-')
                    if flipped:
                        count += 1

            f.write_output(count, case_num)


