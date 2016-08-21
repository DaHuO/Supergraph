import StringIO

import itertools

from ecodejam.input_parser import *


def solve_n(n, top):
    if n == 0:
        return top

    if top == "P":
        a = "P"
        b = "R"
    if top == "R":
        a = "R"
        b = "S"
    if top == "S":
        a = "S"
        b = "P"

    a_word = solve_n(n - 1, a)
    b_word = solve_n(n - 1, b)

    if a_word < b_word:
        return a_word + b_word
    return b_word + a_word


def solve(case_index):
    print case_index
    n = read_int()
    r = read_int()
    p = read_int()
    s = read_int()
    next_line()

    opts = sorted([solve_n(n, "P"), solve_n(n, "R"), solve_n(n, "S")])

    for opt in opts:
        if opt.count("R") == r and opt.count("S") == s and opt.count("P") == p:
            return opt
    return "IMPOSSIBLE"

    # return "{:.10}".format(max(tie_prob_for_option(k, option) for option in itertools.combinations(probs, k)))


SAMPLE = """
4
1 1 1 0
1 2 0 0
2 1 1 2
2 2 0 2
"""

if __name__ == "__main__":
    set_parsed_input(
        StringIO.StringIO(SAMPLE)
    )
    run_solver(solve)
