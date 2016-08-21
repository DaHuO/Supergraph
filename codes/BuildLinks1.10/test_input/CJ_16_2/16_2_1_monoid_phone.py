#!/usr/bin/env python2
import sys
from collections import defaultdict

MARKS_1 = {
    'G': ("EIGHT", '8'),
    'U': ("FOUR", '4'),
    'W': ("TWO", '2'),
    'X': ("SIX", '6'),
    'Z': ("ZERO", '0'),
}

MARKS_2 = {
    'F': ('FIVE', '5'),
    'H': ('THREE', '3'),
    'O': ('ONE', '1'),
    'S': ('SEVEN', '7'),
}    

MARKS_3 = {
    'I': ('NINE', '9'),
}

def input_to_cfg(string):
    cfg = defaultdict(int)
    for ch in string:
        cfg[ch] += 1
    return cfg

def process_phase(phase, cfg):
    for marker, (digits, value) in phase.iteritems():
        if marker in cfg and cfg[marker] > 0:
            count = cfg[marker]
            yield str(value) * count
            for dig in digits:
                cfg[dig] -= count


def process(string):
    cfg = input_to_cfg(string)
    # MARKS_1
    m1 = list(process_phase(MARKS_1, cfg))
    # MARKS_2
    m2 = list(process_phase(MARKS_2, cfg))
    # MARKS_3
    m3 = list(process_phase(MARKS_3, cfg))

    assert all(v == 0 for v in cfg.itervalues())
    
    return ''.join(sorted(m1 + m2 + m3))

def main():
    count = int(raw_input())

    for i in xrange(1, count + 1):
        string = raw_input()
        print "Case #{}: {}".format(i, process(string))

if __name__ == '__main__':
    main()
