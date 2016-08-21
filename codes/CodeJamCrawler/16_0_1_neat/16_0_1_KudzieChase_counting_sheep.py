import sys
import itertools


class Output(object):
    def output_data(self, test_case_number, output_text):
        return "Case #%s: %s\n" % (test_case_number, output_text)


def test_and_run(data, number_of_test_cases, f):
    check_str = '0123456789'

    for index in range(int(number_of_test_cases)):
        number_list = []
        output_num_list = []
        input_num = data.readline()

        i = 1

        passed = False
        check_string = list(check_str)

        while check_string != ['', '', '', '', '', '', '', '', '', '']:
            n = int(input_num)
            n *= i
            num = str(n)

            number_list.append(list(num))
            output_num_list.append(num)

            chain = itertools.chain(*number_list)
            num_list = list(chain)

            for number in range(len(num_list)):
                if num_list.count(num_list[number]) > 0:
                    # print check_string.count(num_list[number])
                    if num_list[number] in check_string:
                        # print check_string.index(num_list[number])
                        check_string[check_string.index(num_list[number])] = ''

            i += 1
            print num_list
            print check_string

            if len(number_list) > 2:
                if number_list[0] == number_list[1]:
                    passed = False
                    break

        if check_string == ['', '', '', '', '', '', '', '', '', '']:
            passed = True
        else:
            passed = False

        if not passed:
            output_text = "INSOMNIA"
            # print("Case #%s: %s\n" % (index + 1, output_text))
            output = Output()
            f.write(output.output_data(index + 1, output_text))
        else:
            out_num = output_num_list[-1]
            # print ("Case #%s: %s\n" % (index + 1, out_num))
            f.write(output.output_data(index + 1, out_num))


def initialize(input_file, f):
    data = open(input_file, "r")
    first_line = data.readline()
    number_of_test_cases = first_line

    print("number_of_test_cases:%r" % (number_of_test_cases))

    test_and_run(data, number_of_test_cases, f)


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    f = file(output_file, 'w')
    initialize(input_file, f)


if __name__ == '__main__':
    main()
