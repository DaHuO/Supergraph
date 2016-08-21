import unittest


class TestFallAsleep(unittest.TestCase):

    def test(self):
        self.assertEqual(1, pancake_revenge('-'))
        self.assertEqual(1, pancake_revenge('-+'))
        self.assertEqual(2, pancake_revenge('+-'))
        self.assertEqual(0, pancake_revenge('+++'))
        self.assertEqual(3, pancake_revenge('--+-'))
        self.assertEqual(3, pancake_revenge('-----------+-'))
        self.assertEqual(1, pancake_revenge('-----------++'))


def pancake_revenge(pancakes):
    last_pancake = pancakes[-1]
    previous_pancake = pancakes[0]
    total = 0 if last_pancake == '+' else 1

    for current_pancake in pancakes[1:]:
        if current_pancake != previous_pancake:
            # flip
            total += 1
            previous_pancake = current_pancake

    return total

if __name__ == '__main__':
    should_test = False
    if should_test:
        unittest.main()
    else:
        # file_name = 'B-small-attempt0'
        file_name = 'B-large'
        with open('%s.in' % file_name, 'r') as cases_in:
            with open('%s.out' % file_name, 'w') as cases_out:
                total_cases = int(cases_in.next()[:-1])
                case_number = 0
                for case_str in cases_in:
                    case_number += 1
                    case_input = case_str[:-1]
                    case_output = 'Case #%s: %s' % (case_number, pancake_revenge(case_input))
                    print case_output
                    cases_out.write('%s\n' % case_output)
