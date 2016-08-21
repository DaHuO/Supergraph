from math import ceil


def getNumberByBase(digits, base):
    result = 0
    for x in digits:
        result = result * base + x

    return result


class Case:
    @classmethod
    def parse(cls, line):
        k, c, s = map(int, line.split(' '))
        return cls(k, c, s)

    def __init__(self, k, c, s):
        self.k = k
        self.c = c
        self.s = s

    def solve(self):
        k = self.k
        c = self.c
        s = self.s

        minimumTiles = ceil(k / c)

        if s < minimumTiles:
            return ["IMPOSSIBLE"]

        finalIndexes = []
        originalIndexes = list(range(k))*2
        for i in range(minimumTiles):
            indexes = originalIndexes[(i*c): (i+1)*c]
            finalIndexes.append( getNumberByBase(indexes, k) )

        return [x+1 for x in finalIndexes]


def main(finname, foutname=None):
    fin = open(finname, 'r')
    fout = None if foutname==None else open(foutname, 'w')
    count = int(next(fin).strip())
    for i in range(count):
        case = Case.parse(next(fin).strip())
        answer = " ".join(map(str, case.solve()))
        print("Case #{}: {}".format(i+1, answer), file=fout)

if __name__ == '__main__':
    import sys
    main(sys.argv[1], sys.argv[2])
    print("Done!")
