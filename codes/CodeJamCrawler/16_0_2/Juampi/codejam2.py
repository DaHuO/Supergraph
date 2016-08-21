class PancakeStack:
    def __init__(self, stack = []):
        s = []
        for p in stack:
            if p == '+':
                s.append(1)
            else:
                s.append(-1)
        self.stack = s
    def __str__(self):
        return str(self.stack)
    def flip(self, n):
        self.stack[:n] = [p*-1 for p in self.stack[:n]][::-1]
    def is_good(self):
        for p in self.stack:
            if p == -1:
                return False
        return True
    def solve(self, acc):
        if self.is_good():
            return acc
        if self.stack == []:
            return acc
        if self.stack[-1] == 1:
            s = PancakeStack()
            s.stack = self.stack[:-1]
            return s.solve(acc)
        elif self.stack[0] == -1:
            self.flip(len(self.stack))
            return self.solve(acc + 1)
        else:
            count = 0
            for p in self.stack:
                if p == 1:
                    count += 1
                else:
                    break
            self.flip(count)
            return self.solve(acc + 1)

def read_data(filename):
    with open(filename) as f:
        num_test_cases = int(f.readline())
        test_cases = []
        for _ in range(num_test_cases):
            test_case = PancakeStack(f.readline().strip())
            test_cases.append(test_case)
    return num_test_cases, test_cases

if __name__ == "__main__":
    num_test_cases, test_cases = read_data("input.in")
    for it in range(num_test_cases):
        test_case = test_cases[it]
        print("Case #{}:".format(it + 1), test_case.solve(0))
