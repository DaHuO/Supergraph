import sys
from copy import copy


def check_majority(P):
    total = sum(P)
    majority = total // 2 + 1
    return not any([p >= majority for p in P])


def options(P):
    for i in range(len(P)):
        P_ = copy(P)
        P_[i] -= 1
        if P_[i] >= 0 and check_majority(P_):
            yield (i, None), P_
        for j in range(len(P)):
            P__ = copy(P_)
            P__[j] -= 1
            if P__[j] >= 0 and check_majority(P__):
                yield (i, j), P__


def select_option(open_set):
    S = 1000000000000000000000000000000000000000000000000
    idx = 0
    for i, (T, path) in enumerate(open_set):
        diff = max(T) - min(T)
        if diff < S:
            idx = i
    R = open_set[idx]
    del open_set[idx]
    return R, open_set


def evacuate_plan(P):
    open_set = [(P, [])]
    while True:
        (T, path), open_set = open_set[0], open_set[1:]
        for step, state in options(T):
            p_ = path + [step]
            if sum(state) == 0:
                final_path = p_
                return final_path
            open_set.append((state, p_))


def evacuate(P):
    plan = evacuate_plan(P)

    def convert(S):
        if S[1] is None:
            return chr(S[0] + 65)
        else:
            return "".join([chr(a + 65) for a in S])

    return [convert(p) for p in plan]


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        T = int(f.readline())
        for idx, N_ in enumerate(f):
            N = int(N_)
            splits = f.readline().split()
            P = [(chr(i+65), int(a)) for i, a in enumerate(splits)]
            P = [(int(a)) for a in splits]
            print("Case #%d: %s" % (idx+1, " ".join(evacuate(P))))
