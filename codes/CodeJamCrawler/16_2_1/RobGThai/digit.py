from itertools import imap, groupby, izip

def print_case(case_no, answer):
    print 'Case #{case_no}: {answer}' \
        .format(
            case_no = case_no,
            answer = answer
        )

class Decypher():

    def __init__(self):
        self.total = int(raw_input())
        self.spelling = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR',
                         'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

    def remove(self, number, times, groups):
        spelling = self.spelling[number]

        for i in xrange(0, times):
            for c in spelling:
                groups[c] -= 1

                if groups[c] <= 0:
                    groups.pop(c)

    def remove_x(self, groups, x, key):
        result = str(x) * groups[key]
        self.remove(x, groups[key], groups)
        return result

    def remove_0(self, groups):
        return self.remove_x(groups, 0, 'Z')

    def remove_1(self, groups):
        return self.remove_x(groups, 1, 'O')

    def remove_2(self, groups):
        return self.remove_x(groups, 2, 'W')

    def remove_3(self, groups):
        return self.remove_x(groups, 3, 'H')

    def remove_4(self, groups):
        return self.remove_x(groups, 4, 'U')

    def remove_5(self, groups):
        return self.remove_x(groups, 5, 'V')

    def remove_6(self, groups):
        return self.remove_x(groups, 6, 'X')

    def remove_7(self, groups):
        return self.remove_x(groups, 7, 'S')

    def remove_8(self, groups):
        return self.remove_x(groups, 8, 'G')

    def remove_9(self, groups):
        return self.remove_x(groups, 9, 'I')

    def solve(self, case, input):
        result = ''
        current = 0
        groups = {}

        checkers = 'ZWUXSGHVIO'
        funcs = [self.remove_0, self.remove_2, self.remove_4, self.remove_6,
                self.remove_7, self.remove_8, self.remove_3, self.remove_5,
                self.remove_9, self.remove_1]

        for k, c in groupby(sorted(input)):
            groups[k] = len(list(c))

        for c, func in izip(checkers, funcs):
            if c in groups:
                result += func(groups)

        print_case(case, ''.join(sorted(result)))

if __name__ == '__main__':
    d = Decypher()

    for i in xrange(1, d.total+1):
        d.solve(i, raw_input())
