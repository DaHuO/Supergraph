from itertools import product
from itertools import *
from collections import defaultdict, Counter
import sys

sys.setrecursionlimit(1500)


def main(filename):
    f = iter(open(filename, "r").readlines())

    t = int(next(f))
    for e, _ in enumerate(range(t)):
        word = next(f).strip()
        print("Case #{}: {}".format(e+1, find(word)))

def isletinres(word, phrase):
    w = Counter(word)
    new_phrase = phrase.copy()
    for let, count in w.items():
        new_phrase[let] = new_phrase[let] -count

    if any([ i < 0 for i in new_phrase.values()]):
        return False, phrase

    else:
        return True, new_phrase

fig = {
    "ZERO": 0,
    "ONE": 1,
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9
}

def find(rest):

    rest_dict = Counter(rest)

    return find_rec(rest_dict)

def find_rec(rest, res_rec=None):
    # print(rest, res_rec)
    res = res_rec or []

    if sum(rest.values()) == 0:
        return "".join([ str(i) for i in sorted(res_rec)])

    for let, num in fig.items():
        res_copy = res[:]

        isok, new_res_rec = isletinres(let, rest)
        

        if isok:
            res_copy.append(num)

            sol = find_rec(new_res_rec, res_copy)
            if sol is not None:
                return sol




if __name__ == "__main__":

    filename = "test"
    filename = "A-small-attempt0.in"
    # filename = "A-large.in"

    

    main(filename)





