def run_case(input):
    stack, = read_strs(input)
    return do_str(stack, '+', 0)


def do_str(st, target, moves):
    if len(st) == 0:
        return moves
    if len(st) == 1:
        return (moves + 1) if target != st else moves

    # No flip
    nf_end = chars_until_end(st)
    nf_target = st[-1]
    nf_penalty = 1 if nf_target != target else 0
    if nf_end > len(st):
        return moves + nf_penalty
    nf_score = nf_penalty

    # With flip
    flipped = flip(st)
    wf_end = chars_until_end(flipped)
    wf_target = flipped[-1]
    wf_penalty = 1 if wf_target != target else 0
    wf_flip = 1
    wf_score = wf_penalty + wf_flip

    # import pdb; pdb.set_trace()
    if nf_score <= wf_score:
        return do_str(st[:nf_end], nf_target, moves + nf_penalty)
    else:
        return do_str(flipped[:wf_end], wf_target, moves + wf_penalty + wf_flip)


def flip(st):
    return st.replace('-', 'p').\
        replace('+', 'm').replace('m', '-').replace('p', '+')[::-1]


def opp(st):
    return '+' if st == '-' else '-'


def chars_until_end(st):
    rev = st[::-1]
    return len(rev) - rev.find(opp(rev[0]), 1)


##############################
#    CODE JAM BOILERPLATE    #
##############################


def read_ints(input, n=1):
    """ Read n integers from input - all on one line, space separated """
    return (int(st) for st in read_strs(input, n))


def read_strs(input, n=1):
    """ Read n strings from input - all on one line, space separated """
    return input.pop(0).rstrip("\n").split(" ")

# GCJ boiler plate...call run_case for each case given
if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10000)
    lines = sys.stdin.readlines()
    sys.stdin = open('/dev/tty')
    num_cases = int(lines.pop(0))
    for case_num in range(num_cases):
        print("Case #%d: %s" % (case_num + 1, run_case(lines)))
