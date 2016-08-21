class Case:
    @classmethod
    def parse(cls, line):
        x = int(line)
        return Case(x)

    def __init__(self, x):
        self.x = x

    def solve(self):
        x = self.x

        if x == 0:
            return "INSOMNIA"

        digits = set(str(x))

        y = x
        while len(digits) < 10:
            y += x
            digits.update(set(str(y)))

        return y

def main(finname, foutname=None):
    fin = open(finname, 'r')
    fout = None if foutname==None else open(foutname, 'w')
    count = int(next(fin).strip())
    for i in range(count):
        case = Case.parse(next(fin).strip())
        print("Case #{}: {}".format(i+1, case.solve()), file=fout)

    fout.close()

if __name__ == '__main__':
    import sys
    inputFilename = sys.argv[1]
    outputFilename = sys.argv[2]
    main(inputFilename, outputFilename)
