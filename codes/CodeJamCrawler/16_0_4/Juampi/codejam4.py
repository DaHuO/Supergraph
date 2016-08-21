def solve(test_case):
    K, C, S = test_case
    if S < K:
        return "IMPOSSIBLE"
    tiles = []
    for i in range(K):
        tiles.append(str(i*K**(C - 1) + 1))
    return ' '.join(tiles)

def read_data(filename):
    with open(filename) as f:
        num_test_cases = int(next(f))
        test_cases = []
        for _ in range(num_test_cases):
            K, C, S = [int(n) for n in next(f).split()]
            test_case = (K, C, S)
            test_cases.append(test_case)
    return num_test_cases, test_cases

if __name__ == "__main__":
    num_test_cases, test_cases = read_data("input.in")
    for it in range(num_test_cases):
        test_case = test_cases[it]
        print("Case #{}:".format(it + 1), solve(test_case))
