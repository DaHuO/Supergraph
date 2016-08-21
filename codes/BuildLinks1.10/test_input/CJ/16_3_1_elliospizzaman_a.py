"""
Google Code Jam 2016 Round 1C
Problem A. NAME
By EJM Software 2016
"""
class Jammer(object):
    """Code Jam Helper Class"""
    def __init__(self, input_handle, output_handle):
        self.input_handle = input_handle
        self.output_handle = output_handle
        self.case_num = 1
    def read_string(self):
        """Reads one line as a string"""
        return self.input_handle.readline().rstrip("\n")
    def read_array(self):
        """Reads one line as an array"""
        return self.read_string().split()
    def write_case(self, solution):
        """Write one case to the output handle"""
        self.output_handle.write("Case #%i: %s\n"%(self.case_num, solution))
        self.case_num += 1

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def solve(jam):
    casecount = int(jam.read_string())
    for casenum in xrange(casecount):
        solution = ""
        n = int(jam.read_string())
        p = map(int, jam.read_array())
        senators = sum(p)
        while senators>0:
            # Always evacuate one senator
            nxt = p.index(max(p))
            p[nxt] -= 1
            solution += LETTERS[nxt]
            senators -= 1
            # Try to evacuate another senator
            nxt = p.index(max(p))
            if not(p.count(p[nxt])==2 and nxt == senators/2):
                p[nxt] -= 1
                solution += LETTERS[nxt]
                senators -= 1
            solution += " "
        solution.rstrip()
        jam.write_case(solution)

if __name__=="__main__":
    import sys
    if len(sys.argv)==3:
        inputh = open(sys.argv[1], "r") if sys.argv[1]!="null" else sys.stdin
        outputh = open(sys.argv[2], "w") if sys.argv[2]!="null" else sys.stdout
        solve(Jammer(inputh, outputh))
    else:
        print "usage: python a.py INPUT_FILE OUTPUT_FILE"
        print "parameters:"
        print "\tINPUT_FILE is the filename of the input. If \"null\", the program will read from stdin."
        print "\tOUTPUT_FILE is the filename of the output. If \"null\", the program will write to stdout."
