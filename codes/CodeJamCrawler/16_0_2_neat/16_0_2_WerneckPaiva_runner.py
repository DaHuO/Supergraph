
class CodeJamRunner(object):

    results = None

    def __init__(self, filename):
        self.results = []

        with open(filename, 'r') as f:
            tests = int(f.readline())
            for _ in xrange(tests):
                params = self.read_test(f)
                result = self.execute(**params)
                self.results.append(result)

    def read_test(self, f):
        raise NotImplementedError()

    def execute(self, *args, **kwargs):
        raise NotImplementedError()

    def print_result(self):
        for (i, result) in enumerate(self.results):
            print "Case #%s: %s" % ((i+1), result)
