from runner.runner import CodeJamRunner

def first_divisor(n):
    if n <= 1: return False
    for i in xrange(2, int(n ** .5) + 1):
        if n % i == 0: return i
        if i > 1000: # taking too long, give up
            return -1
    return 0

def toBase(n, b):
    return sum([b**i*int(c) for i,c in enumerate(n[::-1])])

def coin_jam(length, count):
    nformat = '1{:0'+str(length - 2)+'b}1'
    lower = nformat.format(0)
    numbers = {}
    i = 0
    while len(numbers) < count:
        n_part = toBase(lower[1:-1], 2) + i
        n = nformat.format(n_part)
        divisors = []
        values = []
        for b in xrange(2, 11):
            v = toBase(n, b)
            divisor = first_divisor(v)
            if divisor <= 0:
                break
            values.append(v)
            divisors.append(divisor)
        i += 1
        if len(divisors) < 9:
            continue
        numbers[n] = divisors
    return numbers


class CoinJamRunner(CodeJamRunner):

    def read_test(self, f):
        line = f.readline().replace("\n", "")
        n, j = line.split()
        return {
                "count": int(j),
                "length": int(n)
                }

    def execute(self, **kwargs):
        return coin_jam(**kwargs)

    def print_result(self):
        for (i, result) in enumerate(self.results):
            print "Case #%s:" % (i+1)
            for (n, divisors) in result.items():
                print "%s %s" % (n, " ".join(map(str, divisors)))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print "Usage: python coin_jam.py <filename>"
        exit()
    runner = CoinJamRunner(sys.argv[1])
    runner.print_result()