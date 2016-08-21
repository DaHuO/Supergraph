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


PARTIES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def pl(i):
    return PARTIES[i]


def get_evac_seq(senators):
    seq = []
    while len(senators) > 0:
        senators.sort()
        nparties = len(senators)
        assert nparties > 1
        (n0, p0) = senators.pop()
        (n1, p1) = senators[-1]
        if (n0 - n1 >= 2):
            evac = pl(p0) * 2
            n0 -= 2
            senators.append((n0, p0))
        else:
            evac = pl(p0)
            n0 -= 1
            if nparties == 2:
                if n0 + 1 == n1:
                    evac += pl(p1)
                    senators.pop()
                    n1 -= 1
                    if n1 > 0:
                        senators.append((n1, p1))
                if n0 > 0:
                    senators.append((n0, p0))
            else:
                n2, p2 = senators[-2]
                if n0 == n1 and n2 < n1:
                    evac += pl(p1)
                    senators.pop()
                    n1 -= 1
                    if n1 > 0:
                        senators.append((n1, p1))
                if n0 > 0:
                    senators.append((n0, p0))

        seq.append(evac)
    return seq


def solve(P):
    senators = [(p, i) for i, p in enumerate(P)]
    return get_evac_seq(senators)


if __name__ == '__main__':
    input_name = sys.argv[1] if len(sys.argv) > 1 else 'A-tiny-practice.in'
    rw = ReadWrite(input_name, formatter=make_seq_fmt(' '))
    T = rw.read_line(int)
    for t in range(T):
        n = rw.read_line(int)
        p = tuple(rw.read_line(int))
        assert (len(p) == n)
        rw.write_case(solve(p))
