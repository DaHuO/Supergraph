import sys

def slip(state, n_to_slip):
    return ''.join(['-' if c == '+' else '+' for c in state[:n_to_slip]][::-1]) + state[n_to_slip:]

T = int(raw_input())
for case_idx in xrange(1, T+1):
    sys.stdout.write("Case #{}: ".format(case_idx))
    s = raw_input().strip()
    states = {s}
    ans = '+' * len(s)
    for i in xrange(0, 1000000000000):
        if ans in states:
            print i
            break
        new_states = set()
        for state in states:
            for n_to_slip in xrange(1, len(s) + 1):
                new_states.add(slip(state, n_to_slip))
        states = new_states


