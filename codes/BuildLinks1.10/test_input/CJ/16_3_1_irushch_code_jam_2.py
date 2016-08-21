"""
2 2
3 2 2
1 1 2
2 3 1
"""

import string


POL = list(string.ascii_uppercase)


def balance(politics):
    if sum(politics) == 0:
        return [0]
    return [(x * 100.0) / sum(politics) for x in politics]


def no_one_has_majority(balance):
    return max(balance) <= 50


def save_politic(politics):
    mx = max(politics)
    if mx == 0:
        return ''
    index = politics.index(mx)
    politics[index] = politics[index] - 1
    return POL[index], index


def evacuate(num_pol, politics):
    result = []
    while max(politics) > 0:
        first, _ = save_politic(politics)
        second, index = save_politic(politics)
        if not no_one_has_majority(balance(politics)):
            politics[index] = politics[index] + 1
            result.append(first)
        else:
            result.append(first + second)

    return result


def main():
    # raw_input() reads a string with a line of input,
    # stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        num_pol = int(raw_input())
        inp = [int(s) for s in raw_input().split(" ")]
        # read a list of integers, 2 in this case
        res = evacuate(num_pol, inp)
        print "Case #{}: {}".format(i, ' '.join(res))
        # check out .format's specification for more formatting options


if __name__ == "__main__":
    main()
