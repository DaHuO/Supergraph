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
                self.process_case()
            else:
                self.lines = []
                for line_no in xrange(self.no_of_lines_in_input):
                    self.lines.append(raw_input())
                self.process_case()



class ASOl(GcjBase):

     def process_case(self):
        P = self.lines[0]
        S = self.lines[1].split(' ')
        psum = 0
        DS = []
        cur_ch = ord('A')
        for i, x in enumerate(S):
            DS.append([chr(cur_ch + i), int(x)])
            psum += int(x)

        if self.debug_sol:
            print DS
        DS.sort(key=lambda y: y[1], reverse=True)
        if self.debug_sol:
            print S
            print DS

        sol = []
        while len(DS) > 1:
            diff = psum - 2 * DS[1][1]
            if diff == 0:
                while DS[0][1] != 0:
                    sol.append(DS[0][0]+DS[1][0])
                    DS[0][1] -= 1
                    DS[1][1] -= 1
                DS.pop(0)
                DS.pop(0)
                break

            for i in xrange(min(diff, DS[0][1])):
                sol.append(DS[0][0])

            DS[0][1] -= diff
            if DS[0][1] <= 0:
                DS.pop(0)

            DS.sort(key=lambda y: y[1], reverse=True)
            psum = 0
            for x in DS:
                psum += x[1]
        if DS:
            while DS[0][1] != 0:
                sol.append(DS[0][0])
                DS[0][1] -= 1
        self.print_sol(' '.join(sol))
ASOl(False, 2)
