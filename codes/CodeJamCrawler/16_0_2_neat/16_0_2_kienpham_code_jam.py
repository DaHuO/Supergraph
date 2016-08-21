import sys

class CodeJam:
    def __init__(self, args):
        if(len(args)) == 1:
            self.input_file = sys.argv[0].replace('./', '').replace('.py', '_sample.in')
        else:
            self.input_file = sys.argv[1]

        self.output_file = self.input_file.replace('.in', '.out')

    def run(self):
        with open(self.input_file, 'r+') as f:
            data = f.read().splitlines()
            test_cases = data.pop(0)

            return int(test_cases), data

    def print_output(self, case_number, answer):
        res = "Case #{}: {}".format(case_number, answer)

        with open(self.output_file, 'a') as f:
            print(res)
            f.writelines(res)
