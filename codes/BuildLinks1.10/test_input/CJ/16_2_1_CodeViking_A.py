import os, sys


def make_fmt(formatter, specials):
    return lambda item: specials.get(item, formatter(item))


def make_seq_fmt(sep, item_fmt=str):
    return lambda items: sep.join([item_fmt(i) for i in items])


class ReadWrite:
    """
    Utility class for Google CodeJam.
    Handles input/output, counting and formatting cases.
    """

    def __init__(self, file_name=None, verbose=True, formatter=str):
        self.verbose = verbose
        self.formatter = formatter
        if file_name is None:
            self.in_file = sys.stdin
            self.out_file = sys.stdout
        else:
            self.in_file = open(file_name)
            self.out_file = open(os.path.splitext(file_name)[0] + '.out', 'w')
        self._case_idx = 1

    def msg(self, output, end='\n'):
        sys.stderr.write(str(output) + end)

    def read_line(self, *types):
        """
        Read a line from the input file.  Divide that line into
        space-separated words, use *types to convert each word in order.  If
        there are more words in the line than provided types, the last
        provided type will be used for all subsequent words.

        """
        words = self.in_file.readline().strip().split()
        if len(words) == 1:
            return types[0](words[0])
        return [types[min(i, len(types) - 1)](words[i])
                for i in range(len(words))]

    def write_case(self, output, pfx_char=' '):
        pfx = "Case #%d:" % self._case_idx
        self._case_idx += 1
        text = pfx + pfx_char + self.formatter(output)
        self.out_file.write(text + '\n')
        if self.verbose:
            self.msg(text)
        else:
            self.msg(pfx)


DIGITS = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
          "EIGHT", "NINE")

INDICATORS_0 = ("Z", None, "W", None, "U", None, "X", None, "G", None)
INDICATORS_1 = (None, "O", None, "T", None, "F", None, "S", None, "N")


def take_one(digit, letters):
    result = []
    t = list(letters)
    for c in DIGITS[digit]:
        if c not in t:
            return (None, letters)
        t.remove(c)
    return (digit, tuple(t))


def take_many(digit, ind, letters):
    result = []
    while len(letters) > 0 and ind in letters:
        d, letters = take_one(digit, letters)
        if d is None:
            return (result, letters)
        result.append(d)
    return (result, letters)


def solve(letters):
    result = []
    digits = []
    for indicators in (INDICATORS_0, INDICATORS_1):
        for i in range(10):
            ind = indicators[i]
            if ind is not None:
                (digits, letters) = take_many(i, ind, letters)
                result.extend(digits)
    result.sort()
    assert len(letters) == 0
    return ''.join([str(d) for d in result])


if __name__ == '__main__':
    input_name = sys.argv[1] if len(sys.argv) > 1 else 'A-small-attempt0.bin'
    rw = ReadWrite(input_name, formatter=str)
    T = rw.read_line(int)
    for t in range(T):
        S = tuple(rw.read_line(str))
        rw.write_case(solve(S))
