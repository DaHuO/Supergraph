from __future__ import absolute_import, division
import bisect
from collections import OrderedDict

input_file = 'A-large.in'
output_file = 'A-large.out'
FIN = open(input_file, "r")
FOUT = open(output_file, "w")


class Jam:
    def __init__(self):
        pass

    buf = None
    identity = lambda x: x

    @classmethod
    def _read_line(cls):
        line = FIN.readline().strip('\n')
        return line

    @classmethod
    def _read_line_int(cls):
        return int(cls._read_line())

    @classmethod
    def tokens(cls, conv=identity):
        line = cls._read_line()
        array = line.split()
        return [conv(i) for i in array]

    current_case = 0

    @classmethod
    def case(cls):
        cls.current_case += 1
        return b'Case #{}:'.format(cls.current_case)

class Mat:
    def __init__(self):
        pass

    @classmethod
    def is_even(cls, x):
        if (x & 1) == 0:
            return True
        else:
            return False

    @classmethod
    def odd_ones(cls, x):

        x ^= x >> 16
        x ^= x >> 8
        x ^= x >> 4
        x ^= x >> 2
        x ^= x >> 1

        return x & 1


def ind_to_alphabet(ind):
    asc = ind + 65
    return chr(asc)


def solve():
    array = Jam.tokens(int)
    res = ''
    current_map = {}
    for p in range(len(array)):
        party = ind_to_alphabet(p)
        num = array[p]
        if num not in current_map:
            current_map[array[p]] = []
        current_map[num].append(party)

    keys = sorted(current_map.keys(), reverse=True)
    while len(keys):
        current_array = current_map[keys[0]]
        is_two = len(current_array) >= 2
        for ind in range(2):
            if ind < len(current_array):
                res += current_array[ind]
            if keys[0] == 1 and len(current_array) == 3:
                is_two = False
                break

        res += ' '

        if is_two:
            transfer = current_array[:2]
            del current_array[:2]
        else:
            transfer = current_array[:1]
            del current_array[:1]

        next_key = keys[0]-1
        if len(current_array) <= 0:
            del keys[0]
        if next_key > 0:
            if next_key in current_map:
                current_map[next_key].extend(transfer)
            else:
                keys.append(next_key)
                keys = sorted(keys, reverse=True)
                current_map[next_key] = transfer

    res = res[:-1]
    return res


def main():
    T = Jam._read_line_int()
    for i in range(T):
        N = Jam._read_line_int()
        # print("{} {}\n".format(Jam.case(), solve()))
        FOUT.write("{} {}\n".format(Jam.case(), solve()))
        FOUT.flush()
    FOUT.close()

main()
