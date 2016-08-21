__author__ = 's16624'

import argparse


class InDataHandler (object):

    def __init__(self, file):
        self.numberOfTestCases = None
        self.data = []
        self.file = file

    def read_file(self):
        with open(self.file) as testData:

            first_line = True
            for line in testData:
                if first_line:
                    self.numberOfTestCases = line
                    first_line = False
                else:
                    self.data.append(line.rstrip())


class OutDataHandler (object):

    def __init__(self, file):
        self.case_string = 'Case '
        self.colon_string = ':'
        self.new_line = '\n'
        self.file = file

    def write_file(self, results_list):

        test_nbr = 1
        with open(self.file, 'w') as outfile:
            for result in results_list:
                line_string = '#'.join((self.case_string, str(test_nbr)))
                line_string = ''.join((line_string, self.colon_string))
                line_string = ' '.join((line_string, str(result)))
                line_string = ''.join((line_string, self.new_line))
                outfile.write(line_string)

                test_nbr += 1


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    parser.add_argument('outfile')
    args = parser.parse_args()

    input_file = InDataHandler(args.infile)
    output_file = OutDataHandler(args.outfile)

    input_file.read_file()

    results = []
    for test_case in input_file.data:
        N = int(test_case)
        number_digits_found = 0
        last_digits = 0
        digits = []
        for i in range(10):
            digits.append(0)

        x = 1
        while True:
            current_digits = list(str(N * x))

            for index in current_digits:
                digits[int(index)] = 1
            number_digits_found = sum(digits)

            if number_digits_found == 10:
                results.append(''.join(current_digits))
                break
            elif current_digits == last_digits:
                results.append('INSOMNIA')
                break

            last_digits = current_digits
            x += 1

    output_file.write_file(results)