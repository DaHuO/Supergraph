from operator import sub

def readint(): return int(raw_input())


T = readint()

FILTER_ONE = {
    'Z': [0, 'ZROE'],
    'X': [6, 'XSI'],
    'W': [2, 'WTO'],
    'U': [4, 'UROF'],
    'G': [8, 'TIHGE'],
}

FILTER_TWO = {
    'S': [7, 'VSNEE'],
    'O': [1, 'ONE'],
    'H': [3, 'TRHEE'],
    'F': [5, 'VIFE'],
}

FILTER_THREE = {
    'N': [9, 'NNIE'],
}


def do_filter(s, s_filter, is_three=False):
    nums = []
    to_remove = []
    for k, v in s_filter.iteritems():
        n = s.count(k)
        n = n/2 if is_three else n
        nums.extend([v[0]] * n)
        to_remove.extend(v[1] * n)

    for i in to_remove:
        s.remove(i)

    return nums, s
    # return number answer and filtered s


for t in xrange(1, T + 1):
    S = list(raw_input())
    s = sorted(S, reverse=True)

    number = []

    nums, s = do_filter(s, FILTER_ONE)
    number.extend(nums)

    nums, s = do_filter(s, FILTER_TWO)
    number.extend(nums)

    nums, s = do_filter(s, FILTER_THREE, True)
    number.extend(nums)

    number.sort()
    num_str = ''.join(str(x) for x in number)
    print "Case #%d: %s" % (t, num_str)