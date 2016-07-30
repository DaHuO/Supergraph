# pylint: disable=missing-docstring
import sys


class match:
    def __init__(self, winner, a=None, b=None):
        self.winner = winner
        if a is not None:
            if str(a) > str(b):
                a, b = b, a
        self.a = a
        self.b = b

    def __str__(self):
        if self.a is None:
            return self.winner
        return str(self.a) + str(self.b)


def problem(n, r, p, s):
    R = [match('R') for _ in range(r)]
    P = [match('P') for _ in range(p)]
    S = [match('S') for _ in range(s)]
    for run in range(n):
        new_R = []
        new_P = []
        new_S = []
        if len(R) + len(P) < len(S):
            return "IMPOSSIBLE"
        if len(R) + len(S) < len(P):
            return "IMPOSSIBLE"
        if len(S) + len(P) < len(R):
            return "IMPOSSIBLE"
        while len(R) + len(P) != len(S):
            new_P.append(match("", R.pop(0), P.pop(0)))
        while len(R) > 0:
            new_R.append(match("", R.pop(0), S.pop(0)))
        while len(P) > 0:
            new_S.append(match("", P.pop(0), S.pop(0)))
        R = sorted(new_R, key=str)
        P = sorted(new_P, key=str)
        S = sorted(new_S, key=str)
    return str((R + P + S)[0])



def nextline(input_file):
    data = ""
    while not data:
        data = input_file.readline()
    return data[:-1]


def main():
    result = ""
    with sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r') as infile:
        number = int(nextline(infile))
        for run in range(number):
            case = nextline(infile).split(" ")
            case = [int(c) for c in case]
            n, r, p, s = case
            result += 'Case #{}: {}\n'.format(1 + run, problem(n, r, p, s))

    if len(sys.argv) == 1:
        print(result, end='')
    else:
        with open(sys.argv[1].replace('in', 'sol'), 'w') as result_file:
            result_file.write(result)

if __name__ == '__main__':
    main()
