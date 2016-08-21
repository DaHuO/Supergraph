INPUT = "D-small-attempt0.in"
OUTPUT = "small-response.txt"

def map_to_position(generation, length):
    value = (length ** (generation) - 1) / (length - 1)
    return [str(index * value + 1) for index in range(length)]

def solve(inputf, outputf):
    with open(inputf) as f:
        with open(outputf, 'w') as w:
            T = int(f.readline())
            for testcase in range(1, T+1):
                K,C,S = map(int, f.readline().split())
                if K == 1 and S == 1:
                    w.write("Case #{0}: 1".format(testcase))
                else:
                    w.write("Case #{0}: {1}".format(testcase, " ".join(map_to_position(C, K))))
                w.write("\n")

solve(INPUT, OUTPUT)
