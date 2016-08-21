#!/usr/bin/python3.4

__author__ = 'purplebear'


class FileIO(object):
    """
    Utility to interact with input/output files.
    """

    def __init__(self, input_filename='input.txt', output_filename='output.txt'):
        """
        set the input and output file names.
        """
        self._input = input_filename
        self._output = output_filename
        self._fin = open(self._input, 'r')
        self._fout = open(self._output, 'w')

    def get_row(self):
        """
        get a line row.
        """
        return self._fin.readline().strip('\n').strip(' ')

    def get_int(self):
        return int(self.get_row())

    def get_str_arrays(self):
        """
        get a string array from a line row read from file.
        """
        return self._fin.readline().strip('\n').strip(' ').split(' ')

    def get_int_arrays(self):
        return map(lambda x: int(x), self.get_str_arrays())

    def get_float_arrays(self):
        return map(lambda x: float(x), self.get_str_arrays())

    def write(self, stuffs):
        self._fout.write(stuffs)

    def close(self):
        """
         close used resources.
        """
        self._fin.close()
        self._fout.close()


def revenge(row):
    """
    The pattern can be seen, as counting the number of changes of 
    sign from right to left.
    """
    row_len = len(row)
    i = row_len - 1
    prev_sign = '+'
    result =  0
    while i >= 0:
        sign = row[i]
        if sign != prev_sign:
            result += 1
        prev_sign = sign
        i -= 1
    return result


if __name__ == '__main__':
    # input_file = '../inputs/B-test01.in'
    # input_file = '../inputs/B-small-attempt0.in'
    input_file = '../inputs/B-large.in'
    output_file = 'output.txt'

    fr = FileIO(input_file, output_file)

    # read number of test cases
    n_cases = int(fr.get_row())
    # print('number of test cases: %d' % (n_cases,))

    for n in range(n_cases):
        row = fr.get_row()
        # print(row)
        result = revenge(row)
        fr.write('Case #%d: %s\n' % (n + 1, result,))
    fr.close()
