
from __future__ import print_function


def solve(n):
    digits = set()

    for i in range(1, 100):
        digits.update(str(n * i))
        if len(digits) == 10:
            return i
    return None


def main():
    # maxsteps = 0
    # for i in range(10000000):
    #     result = solve(i)
    #     if result is None:
    #         print(i, ">> inf steps >> INSOMNIA")
    #     else:
    #         n, steps = result
    #         if steps > maxsteps:
    #             maxsteps = steps
    #         print(i, ">>", steps, "steps >>", n * steps)
    # print(maxsteps)
    # return
    t = int(raw_input())
    for i in range(t):
        n = int(raw_input())
        steps = solve(n)
        if steps is None:
            result = "INSOMNIA"
        else:
            result = steps * n
        print("Case #{t}: {result}".format(
            t=i + 1,
            result=result
        ))


if __name__ == "__main__":
    main()
