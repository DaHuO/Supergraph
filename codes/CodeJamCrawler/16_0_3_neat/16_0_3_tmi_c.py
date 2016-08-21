import math
import unittest

should_test = False


class TestFallAsleep(unittest.TestCase):

    def test(self):
        # coin_jam(6, 3)
        # possible_numbers(3)
        # possible_numbers(4)
        possible_numbers(32)

        # results = coin_jam(16, 5)
        # for res in results:
        #     print res


def list_to_jam_number(l):
    return '1%s1' % ''.join([str(i) for i in l])


def possible_numbers(length):
    max_number = pow(2, length - 2)
    for i in xrange(max_number):
        yield '1%s1' % format(i, 'b').zfill(length - 2)


def find_easy_divisors(n):
    max_check = int(math.sqrt(n))
    max_check = int(math.sqrt(max_check))
    for i in xrange(3, max_check + 1, 2):
        if n % i == 0:
            return i

def find_divisor(n):
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i


def find_divisors(bases, number):
    divisors = []
    for base in bases:
        rebased_number = int(number, base)

        if rebased_number == 2:
            return None
        if rebased_number % 2 == 0:
            divisors.append(2)
            continue
        divisor = find_easy_divisors(rebased_number)
        if divisor is None:
            return None
        divisors.append(divisor)

    return divisors


def coin_jam(length, goal):
    bases = range(2, 11)
    output = {}
    for number in possible_numbers(length):
        print number
        divisors = find_divisors(bases, number)
        if divisors is not None:
            print divisors
            output[number] = divisors
            if len(output) == goal:
                return output


if __name__ == '__main__':
    if should_test:
        unittest.main()
    else:
        problem_name = 'C'
        # file_name = '%s-small-attempt0' % problem_name
        file_name = '%s-large' % problem_name
        with open('%s.in' % file_name, 'r') as cases_in:
            with open('%s.out' % file_name, 'w') as cases_out:
                total_cases = int(cases_in.next()[:-1])
                case_number = 0
                for case_str in cases_in:
                    case_number += 1
                    case_input = case_str[:-1]
                    case_output = coin_jam(32, 500)
                    case_output_str = 'Case #1:'
                    cases_out.write('%s\n' % case_output_str)
                    for k, v in case_output.iteritems():
                        cases_out.write('%s %s\n' % (k, ' '.join([str(d) for d in v])))
