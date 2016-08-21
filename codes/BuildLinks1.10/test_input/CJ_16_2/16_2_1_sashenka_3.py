from collections import defaultdict

class Number:
    def __init__(self, num, s, key):
        self.num = num
        self.s = s
        self.key = key

    def is_in(self, d):
        return d[self.key]

    def remove(self, d):
        for c in self.s:
            d[c] -= 1
        return d


def solve_one(input, numbers):
    line = input.readline().strip()
    d = defaultdict(int)
    for c in line:
        d[c] += 1
    result = []
    for number in numbers:
        while(number.is_in(d)):
            result.append(number.num)
            d = number.remove(d)
    result.sort()
    return ''.join(map(str, result))

def main():
    numbers = [
        Number(0, "ZERO", "Z"),
        Number(6, "SIX", "X"),
        Number(4, "FOUR", "U"),
        Number(2, "TWO", "W"),
        Number(7, "SEVEN", "S"),
        Number(8, "EIGHT", "G"),
        Number(3, "THREE", "T"),
        Number(1, "ONE", "O"),
        Number(5, "FIVE", "F"),
        Number(9, "NINE", "I")
            ]
    with open('input.txt') as input:
        cases = int(input.readline())
        with open('output.txt', 'w') as output:
            for case in xrange(cases):
                print case + 1
                output.write("Case #%s: %s\n" % (case + 1, solve_one(input, numbers)))


if __name__ == '__main__':
    main()