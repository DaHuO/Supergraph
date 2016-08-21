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

class RevengeOfthePanCake(GcjBase):

    def __init__(self, *args):
        self.cur_stack = None
        self.flips = 0
        self.stack_len = 0
        super(RevengeOfthePanCake, self).__init__(*args)

    def flip_pan_cakes(self, index):
        self.flips += 1
        for x in xrange(index, -1, -1):
            if self.cur_stack[x] == '-':
                self.cur_stack[x] = '+'
            else:
                self.cur_stack[x] = '-'
        self.debugger(self.cur_stack)

    def re_arrange_pancakes(self):
        index = -1
        neg_start = self.cur_stack[0] == '-'
        for i in self.cur_stack:
            index += 1
            if neg_start and i == '+':
                self.flip_pan_cakes(index-1)
                self.re_arrange_pancakes()
                break
            elif not neg_start and i == '-':
                self.flip_pan_cakes(index-1)
                self.re_arrange_pancakes()
                break
            elif neg_start and index == self.stack_len-1:
                self.flip_pan_cakes(self.stack_len-1)
                break



    def process_case(self):
        init_stack = self.lines
        self.flips = 0
        self.stack_len = len(init_stack)
        self.cur_stack = [x for x in init_stack]
        self.re_arrange_pancakes()
        self.print_sol(self.flips)
try:
    debug_flag = sys.argv[1]
except:
    debug_flag = 'f'

rptpc = RevengeOfthePanCake(debug_flag == 't', 1)
