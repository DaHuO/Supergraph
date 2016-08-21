import sys

def read_case(line):
    return int(line.strip())


def make_solution(N):
    if N == 0:
        return "INSOMNIA"

    seen = [False] * 10
    i = 1
    while True:
        for c in str(i*N):
            seen[int(c)] = True
        if all(seen):
            return i*N
        i += 1


if __name__ == "__main__":
    f = sys.stdin
    #f = open("samples.text")
    count = int(f.readline())
    for c in range(count):
        case = read_case(f.readline())
        solution = make_solution(case)
        print("Case #{}: {}".format(c+1, solution))