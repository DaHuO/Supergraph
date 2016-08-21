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


def get_digit_set(number):
	result_set = set()
	number_str = str(number)
	for digit in number_str:
		result_set.add(digit)
	return result_set


def do_something(answer):
    n = 1
    in_loop = True
    n_limit = 1000
    result = None
    not_moving_limit = 100
    prev_len_seen_set = 0
    # shortcut for even numbers, there's no chance for even numbers
    # to produce odd numbers...
    # if answer % 2 == 0:
    # 	return 'INSOMNIA'

    seen_set = set()
    while in_loop and n <= n_limit:
        number = n * answer
        digit_set = get_digit_set(number)
        seen_set = seen_set.union(digit_set)
        len_seen_set = len(seen_set)
        # print('  %d, %d, %d, %s' %(n, number, len_seen_set, str(seen_set),))
        if len_seen_set == 10:
            in_loop = False
            result = number
        n += 1
        if prev_len_seen_set == len_seen_set:
            not_moving_count += 1
        else:
            not_moving_count = 0
        if not_moving_count < not_moving_limit:
            prev_len_seen_set = len_seen_set
        else:
            return 'INSOMNIA'

    if result is None:
        return 'INSOMNIA'
    else:
        return str(result)


if __name__ == '__main__':

    # input_file = '../inputs/A-test01.in'
    # input_file = '../inputs/A-small-attempt0.in'
    input_file = '../inputs/A-large.in'
    output_file = 'output.txt'

    fr = FileIO(input_file, output_file)

    # read number of test cases
    n_cases = int(fr.get_row())
    # print('number of test cases: %d' % (n_cases,))

    for n in range(n_cases):
        first_answer = fr.get_int()
        result = do_something(first_answer)
        fr.write('Case #%d: %s\n' % (n + 1, result,))
    fr.close()
