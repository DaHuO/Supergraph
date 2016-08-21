import os, sys

sys.setrecursionlimit(500000)


class ReadWrite:
    def __init__(self, file_name=None, verbose=True):
        self.verbose = verbose
        if file_name is None:
            self.in_file = sys.stdin
            self.out_file = sys.stdout
        else:
            self.in_file = open(file_name)
            self.out_file = open(os.path.splitext(file_name)[0] + '.out', 'w')
        self.case_idx = 1

    def msg(self, output, end='\n'):
        sys.stderr.write(str(output) + end)

    def read_line(self, *types, all=None):
        words = self.in_file.readline().strip().split()
        if all is not None:
            return [all(w) for w in words]
        if len(types) == 0:
            return words
        assert (len(words) == len(types))
        if len(types) == 1:
            return types[0](words[0])
        return [t(w) for t, w in zip(types, words)]

    def write_case(self, output, true="YES", false="NO", join='\n'):
        pfx = "Case #%d:" % self.case_idx
        self.case_idx += 1
        if isinstance(output, list):
            text = join.join([pfx] + output)
        elif isinstance(output, bool):
            text = pfx + ' ' + (true if output else false)
        else:
            text = pfx + ' ' + str(output)
        self.out_file.write(text + '\n')
        if self.verbose:
            self.msg(text)
        else:
            self.msg(pfx)


def solve(k, c):
    if c == 1:
        return [i for i in range(0, k)]
    if k == 1:
        return [0]
    b = (k ** (c - 1))
    assert (b == int(b))
    b = int(b)
    bstarts = [b * i for i in range(0, k)]
    boffsets = solve(k, c - 1)
    return [bstarts[i] + boffsets[i] for i in range(0, k)]


if __name__ == '__main__':
    input_name = sys.argv[1] if len(sys.argv) > 1 else 'D-tiny-practice.in'
    rw = ReadWrite(input_name)
    T = rw.read_line(int)
    for t in range(T):
        K, C, S = rw.read_line(int, int, int)
        assert (K == S)
        rw.write_case(' '.join([str(p + 1) for p in solve(K, C)]))
