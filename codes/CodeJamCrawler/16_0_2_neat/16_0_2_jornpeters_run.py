import sys


def count_flips(stack, target):
    if len(stack) == 0:
        return 0
    count = count_flips(stack[1:], stack[0])
    return count + (target != stack[0])


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        num_problems = int(f.readline())
        for i in range(num_problems):
            stack = f.readline().strip()
            print("Case #{}: {}".format(i+1, count_flips(stack[::-1], '+')))
