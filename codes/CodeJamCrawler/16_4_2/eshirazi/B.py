import StringIO

import itertools

from ecodejam.input_parser import *


def get_prob_for_vote(k, option, votes):
    return reduce(lambda x,y: x*y, (prob if vote == 1 else (1-prob) for prob, vote in zip(option, votes)), 1.0)


def tie_prob_for_option(k, option):
    total = 0.0

    # for votes in itertools.product(*[range(2) for i in xrange(k)]):
    #     if votes.count(1) == votes.count(0):
    #         total += get_prob_for_vote(k, option, votes)

    for places in itertools.combinations(range(k), k / 2):
        places = set(places)
        cur = 1.0
        for i in xrange(k):
            cur *= option[i] if i in places else (1-option[i])
        total += cur

    return total


def solve(case_index):
    print case_index
    n = read_int()
    k = read_int()
    next_line()

    probs = [read_float() for i in xrange(n)]
    next_line()

    return "{:.10f}".format(max(tie_prob_for_option(k, option) for option in itertools.combinations(probs, k)))


SAMPLE = """
3
2 2
0.50 0.50
4 2
0.00 0.00 1.00 1.00
3 2
0.75 1.00 0.50
"""

if __name__ == "__main__":
    set_parsed_input(
        StringIO.StringIO(SAMPLE)
    )
    run_solver(solve)
