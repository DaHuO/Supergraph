#!python3

def normalize(S):
    return [True if v == '+' else False for v in S.strip()]


def turn_stack(S):
    return [not v for v in S]


def last_zero_pos(S):
    return (len(S) - list(reversed(S)).index(False) - 1)


def solve(S, step):
    if False not in S:
        return step
    step += 1
    lzp = last_zero_pos(S)
    S = turn_stack(S[0:lzp]) + S[lzp + 1:]
    return solve(S, step)


if __name__ == "__main__":
    import fileinput

    f = fileinput.input()

    T = int(f.readline())
    for case in range(1, T + 1):
        S = str(f.readline())
        S = normalize(S)
        answer = solve(S, 0)
        print("Case #{0}: {1}".format(case, answer))