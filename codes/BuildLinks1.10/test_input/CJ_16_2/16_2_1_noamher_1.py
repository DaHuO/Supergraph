import copy
import sys

################################################################################
import collections

l = {
    'Z': ('ZERO', 0),
    'W': ('TWO', 2),
    'U': ('FOUR', 4),
    'X': ('SIX', 6),
    'G': ('EIGHT', 8)
}

d = {
    1: 'ONE',
    3: 'THREE',
    5: 'FIVE',
    7: 'SEVEN',
    9: 'NINE'
}

def solve(case_inputs):
    w = case_inputs

    w_cnt = collections.Counter()
    for c in w:
        w_cnt[c] += 1

    d_cnt = collections.Counter()
    for k in l.keys():
        (word, digit) = l[k]
        d_cnt[digit] = w_cnt[k]
        for c in word:
            w_cnt[c] -= d_cnt[digit]

    d_cnt = recourse(w_cnt, d_cnt)
    print d_cnt

    s = ''
    for i in range(10):
        s += str(i) * d_cnt[i]
    return s

def recourse(w_cnt, d_cnt):
    if sum(w_cnt.values()) == 0:
        return d_cnt

    for i in d.keys():
        w_copy = copy.deepcopy(w_cnt)
        d_copy = copy.deepcopy(d_cnt)

        ok = True
        for c in d[i]:
            w_copy[c] -= 1
            if w_copy[c] < 0:
                ok = False
        d_copy[i] += 1
        if not ok:
            continue

        r = recourse(w_copy, d_copy)
        if r is not None:
            return r
    return None

################################################################################

def read_case(f):
    return read_word(f)

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')

################################################################################

def read_word(f):
    return next(f).strip()

def read_int(f, b=10):
    return int(read_word(f), b)

def read_letters(f):
    return list(read_word(f))

def read_digits(f, b=10):
    return [int(x, b) for x in read_letters(f)]

def read_words(f, d=' '):
    return read_word(f).split(d)

def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]

def read_floats(f, d=' '):
    return [float(x) for x in read_words(f, d)]

def read_arr(f, R, reader=read_ints, *args, **kwargs):
    return [reader(f, *args, **kwargs) for i in range(R)]

def main():
    if len(sys.argv) != 2:
        print 'usage: python <file_name> <input_file>'
        sys.exit(1)

    with open(sys.argv[1], 'r') as f, open('res', 'w') as w:
        count = read_int(f)
        for i in xrange(1, count + 1):
            case_inputs = read_case(f)
            write_case(w, i, solve(case_inputs))

if __name__ == "__main__":
    main()


