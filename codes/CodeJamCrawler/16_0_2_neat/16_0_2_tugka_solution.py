import sys


def read_case(line):
    return [True if c == "+" else False for c in line.strip()]


def make_solution(cakes):
    def flip(cakes_to_flip):
        position_last_false = [i for i, c in enumerate(cakes_to_flip) if not c][-1]
        flipped = [not c for c in cakes[0:position_last_false+1]] + cakes_to_flip[position_last_false+1:]
        return flipped

    i = 0
    while True:
        if all(cakes):
            return i
        cakes = flip(cakes)
        i += 1

if __name__ == "__main__":
    f = sys.stdin
    #f = open("samples.text")
    count = int(f.readline())
    for c in range(count):
        case = read_case(f.readline())
        solution = make_solution(case)
        print("Case #{}: {}".format(c+1, solution))