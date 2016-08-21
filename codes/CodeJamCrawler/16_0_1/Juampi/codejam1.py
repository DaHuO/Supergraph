class TestCase:
    def __init__(self, n):
        self.n = n
    def solve(self):
        if self.n == 0:
            return "INSOMNIA"
        seen_digits = [0]*10
        k = 0
        while sum(seen_digits) < 10:
            k += 1
            for digit in str(k*self.n):
                seen_digits[int(digit)] = 1
        return k*self.n

def read_data(filename):
    with open(filename) as f:
        num_test_cases = int(f.readline())
        test_cases = []
        for _ in range(num_test_cases):
            test_case = TestCase(int(f.readline()))
            test_cases.append(test_case)
    return num_test_cases, test_cases

if __name__ == "__main__":
    num_test_cases, test_cases = read_data("A-large.in")
    for it in range(num_test_cases):
        test_case = test_cases[it]
        print("Case #{}:".format(it + 1), test_case.solve())
        