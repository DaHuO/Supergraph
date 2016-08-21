def calcDiff(digitsA, digitsB):
    for x, y in zip(digitsA, digitsB):
        if x > y:
            return 1
        if x < y:
            return -1
    return 0

def myCmp(pair1, pair2):
    diff1 = abs(pair1[0] - pair1[1])
    diff2 = abs(pair2[0] - pair2[1])

    if diff1 > diff2:
        return 1
    elif diff1 < diff2:
        return -1


    if pair1[0] > pair2[0]:
        return 1
    elif pair1[0] < pair2[0]:
        return -1

    return pair1[1] - pair2[1]


def findDigits(A, B):
    diff = 0  # 0 - numbers are equal, 1 - first number is larger, -1 - second number is larger

    digitsA = []
    digitsB = []

    for d1, d2 in zip(A, B):
        if d1 == "?" and d2 == "?":
            if diff == 1:
                digitsA.append(0)
                digitsB.append(9)
            elif diff == -1:
                digitsA.append(9)
                digitsB.append(0)
            else:
                #Here could be branching:
                tailA = A[len(digitsA)+1:]
                tailB = B[len(digitsB)+1:]

                yield from findDigits(digitsA + [1] + tailA, digitsB + [0] + tailB)
                yield from findDigits(digitsA + [0] + tailA, digitsB + [1] + tailB)

                digitsA.append(0)
                digitsB.append(0)
        elif d1 == "?":
            digitsB.append(int(d2))
            if diff == 1:
                digitsA.append(0)
            elif diff == -1:
                digitsA.append(9)
            else:
                #Here could be branching:
                tailA = A[len(digitsA)+1:]
                tailB = B[len(digitsB):]

                if int(d2)+1 < 10:
                    yield from findDigits(digitsA + [int(d2)+1] + tailA, digitsB + tailB)
                if int(d2) > 0:
                    yield from findDigits(digitsA + [int(d2)-1] + tailA, digitsB + tailB)

                digitsA.append(int(d2))
        elif d2 == "?":
            digitsA.append(int(d1))
            if diff == 1:
                digitsB.append(9)
            elif diff == -1:
                digitsB.append(0)
            else:
                #Here could be branching:
                tailA = A[len(digitsA):]
                tailB = B[len(digitsB)+1:]

                if int(d1)+1 < 10:
                    yield from findDigits(digitsA + tailA, digitsB + [int(d1)+1] + tailB)
                if int(d1) > 0:
                    yield from findDigits(digitsA + tailA, digitsB + [int(d1)-1] + tailB)

                digitsB.append(int(d1))
        else:
            digitsA.append(int(d1))
            digitsB.append(int(d2))

        diff = calcDiff(digitsA, digitsB)

    yield digitsA, digitsB


def toNumber(digits):
    result = 0
    for x in digits:
        result = result*10 + x

    return result


class Case:
    @classmethod
    def parse(cls, line):
        numbers = line.split(" ")
        assert len(numbers) == 2
        return cls(numbers[0], numbers[1])

    def __init__(self, A, B):
        assert len(A) == len(B)
        self.A = A
        self.B = B

    def solve(self):
        A = self.A
        B = self.B
        count = len(A)

        options = findDigits(list(A), list(B))
        options = [(toNumber(digsA), toNumber(digsB)) for digsA, digsB in options]

        decorated = [(abs(x-y), x, y) for x, y in options]
        decorated.sort()
        options = [(x,y) for diff, x, y in decorated]

        answerX, answerY = options[0]

        return str(answerX).zfill(count) + " " + str(answerY).zfill(count)


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
