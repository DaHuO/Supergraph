"""
Google Code Jam
Round 1B
Problem A.
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
        number_string = jam.read_string()
        digits = [0 for i in range(10)]
        # Easy
        digits[0] = number_string.count("Z")
        digits[2] = number_string.count("W")
        digits[4] = number_string.count("U")
        digits[6] = number_string.count("X")
        digits[8] = number_string.count("G")
        # Less Easy
        digits[3] = number_string.count("T") - digits[8] - digits[2]
        digits[5] = number_string.count("F") - digits[4]
        digits[7] = number_string.count("V") - digits[5]
        digits[9] = number_string.count("I") - digits[8] - digits[6] - digits[5]
        digits[1] = number_string.count("N") - digits[7] - 2*digits[9]
        # Generate solution
        solution = ""
        for i in range(10):
            solution += str(i) * digits[i]
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
