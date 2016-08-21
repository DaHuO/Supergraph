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
            if self.no_of_lines_in_input == 1:
                self.lines = raw_input()
            else:
                self.lines = []
                for line_no in xrange(self.no_of_lines_in_input):
                    print line_no
                    self.lines.append(raw_input())
            self.process_case()

class FractilesSmall(GcjBase):

    def read_input(self):
        # k:len  c:complexity s:sol limit
        k, c, s = self.lines.split(' ')
        self.art_len = int(k)
        self.complexity = int(c)
        self.sol_len = int(s)

    def process_case(self):
        self.read_input()
        if self.art_len == self.sol_len:

            sol = [str(x) for x in xrange(1, self.sol_len+1)]
            self.print_sol(' '.join(sol))


#----------------------------------------------

try:
    debug_flag = sys.argv[1]
except:
    debug_flag = 'f'

fcs = FractilesSmall(debug_flag == 't', 1)
