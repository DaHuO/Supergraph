
from __future__ import print_function


def swap(s):
    return "".join([('-' if c == '+' else '+') for c in s])


def solve(s):
    steps = 0
    while s.count("-") > 0:
        s = s.rstrip("+")

        if len(s) == 0:
            break
        elif s.count("+") == 0:
            steps += 1
            break

        if s.startswith("+"):
            first_minus = s.find("-")
            next_plus = s.find("+", first_minus)
            # 1. Swap first +
            # 2. Swap everything till second +
            s = swap(s[first_minus-1::-1]) + s[first_minus:]
            if next_plus == -1:
                s = swap(s[::-1])
            else:
                s = swap(s[next_plus-1::-1]) + s[next_plus:]
            steps += 2
        else:
            first_plus = s.find("+")
            s = swap(s[first_plus-1::-1]) + s[first_plus:]
            steps += 1
    return steps


def main():
    t = int(raw_input())
    for i in range(t):
        s = raw_input()
        steps = solve(s)
        print("Case #{t}: {result}".format(
            t=i + 1,
            result=steps
        ))
None

if __name__ == "__main__":
    main()
