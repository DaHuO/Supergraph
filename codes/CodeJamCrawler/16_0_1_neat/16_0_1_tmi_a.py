import unittest


class TestFallAsleep(unittest.TestCase):

    def test_fall_asleep(self):
        self.assertEqual(10, fall_asleep(1))
        self.assertEqual(90, fall_asleep(2))
        self.assertEqual(110, fall_asleep(11))
        self.assertEqual(5076, fall_asleep(1692))
        self.assertEqual('INSOMNIA', fall_asleep(0))


def fall_asleep(original_number):
    number = original_number
    digits_seen = set()
    numbers_processed = set()
    while True:
        number_string = str(number)
        digits_seen = digits_seen.union(set(number_string))
        if len(digits_seen) == 10:
            return number
        else:
            number += original_number
            if number in numbers_processed:
                return 'INSOMNIA'
            else:
                numbers_processed.add(number)


if __name__ == '__main__':
    # unittest.main()
    # file_name = 'A-small-attempt1'
    file_name = 'A-large'
    with open('%s.in' % file_name, 'r') as cases_in:
        with open('%s.out' % file_name, 'w') as cases_out:
            total_cases = int(cases_in.next()[:-1])
            case_number = 0
            for case_str in cases_in:
                case_number += 1
                case_input = int(case_str[:-1])
                case_output = 'Case #%s: %s' % (case_number, fall_asleep(case_input))
                print case_output
                cases_out.write('%s\n' % case_output)
