DIGITS_MARKERS = [("Z", "ZERO", 0),
         ("W", "TWO", 2),
         ("U", "FOUR", 4),
         ("X", "SIX", 6),
         ("G", "EIGHT", 8),
         ("R", "THREE", 3),
         ("O", "ONE", 1),
         ("F", "FIVE", 5),
         ("V", "SEVEN", 7),
         ("I", "NINE", 9)]


def calcStats(txt):
    stats = dict()
    for x in txt:
        if x in stats:
            stats[x] += 1
        else:
            stats[x] = 1
    return stats


class Case:
    @classmethod
    def parse(cls, line):
        return Case(line)

    def __init__(self, letters):
        self.letters = letters

    def solve(self):
        letters = self.letters
        digitsStats = calcStats(letters)
        digits = []

        for marker, digitStr, digit in DIGITS_MARKERS:
            if marker in digitsStats and digitsStats[marker] > 0:
                coundDigits = digitsStats[marker]
                digits += [digit]*coundDigits

                substractStats = calcStats(digitStr)
                for letter, count in substractStats.items():
                    digitsStats[letter] -= count*coundDigits
                    assert digitsStats[letter] >= 0

        digits.sort()
        return "".join(str(x) for x in digits)

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
    print("Done!")
