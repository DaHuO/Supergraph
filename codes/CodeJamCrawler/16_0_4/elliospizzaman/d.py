"""
Google Code Jam
2016 Qualification Round
Problem D. Fractiles
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
        k, c, s = map(int, jam.read_array())
        if s < int(k/c + 0.9999999):
            solution = "IMPOSSIBLE"
        else:
            locations = []
            for i in range(0, k, c):
                location = 1
                for j in range(c):
                    location += k**j * min(i+j, k-1)
                locations.append(str(location))
            solution = " ".join(locations)
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
