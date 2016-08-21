from runner.runner import CodeJamRunner

def revenge_pancakes(stack):
    c = stack.count("+-") + stack.count("-+") + (1 if stack[-1] == "-" else 0)
    return c


class RevengePancakesRunner(CodeJamRunner):

    def read_test(self, f):
        line = f.readline().replace("\n", "")
        return {
                'stack': line
                }

    def execute(self, **kwargs):
        return revenge_pancakes(**kwargs)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print "Usage: python revenge_pancakes.py <filename>"
        exit()
    runner = RevengePancakesRunner(sys.argv[1])
    runner.print_result()