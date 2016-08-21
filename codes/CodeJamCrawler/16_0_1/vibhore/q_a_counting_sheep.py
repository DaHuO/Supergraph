import sys

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
            if self.no_of_lines_in_input ==1:
                self.lines = raw_input()
            else:
                self.lines = []
                for line_no in xrange(self.no_of_lines_in_input):
                    print line_no
                    self.lines.append(raw_input())
            self.process_case()


#---------------------------------------------------------------------------------

class CountingSheep(GcjBase):

    def process_case(self):
        ip_no = int(self.lines)
        if ip_no == 0:
            self.print_sol("INSOMNIA")
            return
        digit_flag_mask = 0
        multiplier = 0
        exit_flag = int('1111111111', 2)
        while digit_flag_mask != exit_flag:
            multiplier += 1
            cur_no = ip_no * multiplier
            sol = cur_no
            while cur_no != 0:
                remainder = cur_no % 10
                digit_flag_mask |= 1 << remainder
                cur_no = cur_no / 10
                self.debugger(('multiplier',multiplier, 'remainder, currno',remainder, cur_no))

        self.print_sol(sol)

debug_flag = sys.argv[1]
cs = CountingSheep(debug_flag == 't', 1)
