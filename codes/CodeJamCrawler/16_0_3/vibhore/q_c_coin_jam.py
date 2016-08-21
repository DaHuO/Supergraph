import sys
import math
class GcjBase(object):

    def __init__(self, debug_sol, no_of_lines_in_input ):
        self.lines = None
        self.debug_sol = debug_sol
        self.case_no = 0
        self.no_of_lines_in_input = no_of_lines_in_input
        self.read_input_and_process()

    def debugger(self, msg):
        if self.debug_sol:
            print msg

    def print_sol(self, sol):
        print 'Case #{}: {}'.format(self.case_no, sol)

    def process_case(self):
        raise NotImplementedError

    def read_input_and_process(self):
        no_of_test_cases = int(raw_input())
        for self.case_no in xrange(1, no_of_test_cases+1):
            self.debugger('case_no is ' + str(self.case_no))
            if self.no_of_lines_in_input == 1:
                self.lines = raw_input()
            else:
                self.lines = []
                for line_no in xrange(self.no_of_lines_in_input):
                    print line_no
                    self.lines.append(raw_input())
            self.process_case()


#---------------------------------------------------------------------------------

class CoinJam(GcjBase):
    def __init__(self, *args):
        self.divisor_set = None
        super(CoinJam, self).__init__(*args)

    def print_sol(self, sol):
        print 'Case #{}:'.format(self.case_no)

    def get_factor(self, no):
        # not req for this comp
        # assert no > 0, 'no should be greater than 3'
        sq_no_ceil = int(math.sqrt(no)) + 1
        for i in xrange(2, sq_no_ceil):
            if no % i == 0:
                return i
        return -1


    def process_case(self):
        self.divisor_set = []
        coin_len, combinations_asked = [int(x) for x in self.lines.split(' ')]
        largest_no = int('1'*coin_len, 2)
        smallest_no = int('1'+'0'*(coin_len-2)+'1', 2)
        self.debugger('smallest no {} and largest no{}'.format(smallest_no, largest_no))
        combinations_achieved = 0
        combination_no = 0
        for i in xrange(smallest_no, largest_no + 1, 2):
            combination_no += 1
            self.debugger('-'*40)
            self.debugger('combination no {} , base 2 val {}'.format(combination_no, i))

            factor2 = self.get_factor(i)
            if factor2 == -1:
                self.debugger('exiting as base {} no {}, is prime'.format(2, i))
                continue
            current_coin = bin(i)[2:]

            divisors = [str(factor2)]
            for base in xrange(3, 11):
                base_x_no = int(current_coin, base)
                self.debugger('base {} val {},'.format(base, base_x_no))
                base_x_factor = self.get_factor(base_x_no)
                if base_x_factor == -1:
                    self.debugger('exiting as base {} no {}, is prime'.format(base, base_x_no))
                    break
                else:
                    divisors.append(str(base_x_factor))

            if len(divisors) == 9:
                current_combination = current_coin + ' ' + ' '.join(divisors)
                self.divisor_set.append(current_combination)
                combinations_achieved += 1
                self.debugger('total combinations found = {}, current combination {}'.format(combinations_achieved,
                                                                                    current_combination))

            if combinations_achieved == combinations_asked:
                self.print_sol('')
                for line in self.divisor_set:
                    print line
                if not self.debug_sol:
                    break
        if self.debug_sol:
            print 'all posiblities'
            for line in self.divisor_set:
                self.debugger(line)



try:
    debug_flag = sys.argv[1]
except:
    debug_flag = 'f'

rptpc = CoinJam(debug_flag == 't', 1)
