
class Case:
    @classmethod
    def parse(cls, line):
        return cls(line)

    def __init__(self, pancakes):
        self.pancakes = pancakes

    def solve(self):
        flips = 0
        pancakes = self.pancakes
        for i in range(len(pancakes)-1):
            if pancakes[i] != pancakes[i+1]:
                flips += 1

        if pancakes[-1] == '-':
            flips += 1

        return flips


def main(finname, foutname=None):
    fin = open(finname, 'r')
    fout = None if foutname==None else open(foutname, 'w')
    count = int(next(fin).strip())
    for i in range(count):
        case = Case.parse(next(fin).strip())
        print("Case #{}: {}".format(i+1, case.solve()), file=fout)

if __name__ == '__main__':
    import sys

    main(sys.argv[1], sys.argv[2])
    print("Done!")
