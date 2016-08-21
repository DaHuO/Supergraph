"""
Google Code Jam
ROUND NAME
Problem LETTER. NAME
Copyright EJM Software 2016
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

def solve(jam):
    casecount = int(jam.read_string())
    for casenum in xrange(casecount):
        solution = ""
        n = int(jam.read_string())
        if n==0:
            solution = "INSOMNIA"
        else:
            remaining = map(str, range(10))
            i = 0
            while len(remaining) > 0:
                i += 1
                for digit in str(n*i):
                    if digit in remaining:
                        remaining.remove(digit)
            solution = str(n * i)
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
