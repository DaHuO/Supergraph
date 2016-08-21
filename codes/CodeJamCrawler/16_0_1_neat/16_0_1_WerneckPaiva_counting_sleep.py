from runner.runner import CodeJamRunner

def counting_sheep(n):
    if n == 0:
        return "INSOMNIA"
    numbers = set()
    i = 1
    last = n
    while(len(numbers)<10):
        last = n * i
        numbers |= set(str(last))
        i += 1
    return last

class CountingSheepRunner(CodeJamRunner):

    def read_test(self, f):
        line = f.readline().replace("\n", "")
        return {
                'n': int(line)
                }

    def execute(self, **kwargs):
        return counting_sheep(**kwargs)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print "Usage: python magic_deck.py <filename>"
        exit()
    runner = CountingSheepRunner(sys.argv[1])
    runner.print_result()