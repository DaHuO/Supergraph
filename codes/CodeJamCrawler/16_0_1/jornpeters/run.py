import sys


def count_steps(N):
    num, steps, seen = N, 0, set()
    while True:
        steps += 1
        seen.update(list(str(num)))
        if len(seen) == 10:
            return num
        num += N


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        num_problems = int(f.readline())
        for i in range(num_problems):
            N = int(f.readline().strip())
            if N == 0:
                print("Case #{}: {}".format(i+1, "INSOMNIA"))
            else:
                steps = count_steps(N)
                print("Case #{}: {}".format(i+1, steps))
