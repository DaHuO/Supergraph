import sys
import math

def input_parser(input_path):
    with open(input_path, 'r') as f:
        c = int(f.readline())
        for case in range(c):
            K, C, S = map(int, f.readline().split())
            yield case, (K, C, S)

def get_output_path(input_path):
    return input_path[:-2] + "out"

def output(f, s):
    print(s)
    f.write(s + "\n")

def problem(K, C, S):
    if C == 1:
        if S < K:
            return 'IMPOSSIBLE'
        else:
            return ' '.join(map(str, range(1, K+1)))
    else:
        necessary = math.ceil(K/2)
        if S < necessary:
            return 'IMPOSSIBLE'
        out = []
        to_check = list(range(K))
        while len(to_check) > 0:
            by_area = to_check.pop(0)
            by_pos = to_check.pop(0) if to_check else 0
            out.append(by_area*pow(K,C-1) + by_pos + 1)
        return ' '.join(map(str, out))

def main():
    input_path = sys.argv[1]
    with open(get_output_path(input_path), 'w') as g:
        for case, data in input_parser(input_path):
            out = problem(*data)
            output(g, "Case #{}: {}".format(case+1, out))

if __name__ == "__main__":
    main()

