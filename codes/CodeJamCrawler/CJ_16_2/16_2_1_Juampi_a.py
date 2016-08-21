#!/usr/bin/env python3

"""
Google Code Jam
Round 1B 2016
Problem A
"""

class TestCase:
    def __init__(self, s):
        self.s = s
    def solve(self):
        numbers = []
        s = self.s
        while len(s) > 0:
            if 'W' in s:
                numbers.append(2)
                for c in 'TWO':
                    s = s.replace(c, '', 1)
                continue
            if 'X' in s:
                numbers.append(6)
                for c in 'SIX':
                    s = s.replace(c, '', 1)
                continue
            if 'S' in s:
                numbers.append(7)
                for c in 'SEVEN':
                    s = s.replace(c, '', 1)
                continue
            if 'V' in s:
                numbers.append(5)
                for c in 'FIVE':
                    s = s.replace(c, '', 1)
                continue
            if 'F' in s:
                numbers.append(4)
                for c in 'FOUR':
                    s = s.replace(c, '', 1)
                continue
            if 'Z' in s:
                numbers.append(0)
                for c in 'ZERO':
                    s = s.replace(c, '', 1)
                continue
            if 'R' in s:
                numbers.append(3)
                for c in 'THREE':
                    s = s.replace(c, '', 1)
                continue
            if 'T' in s:
                numbers.append(8)
                for c in 'EIGHT':
                    s = s.replace(c, '', 1)
                continue
            if 'I' in s:
                numbers.append(9)
                for c in 'NINE':
                    s = s.replace(c, '', 1)
                continue
            if 'O' in s:
                numbers.append(1)
                for c in 'ONE':
                    s = s.replace(c, '', 1)
                continue
        numbers.sort()
        return ''.join([str(c) for c in numbers])
        

def read_data(filename):
    with open(filename) as f:
        test_cases = []
        num_test_cases = int(f.readline())
        for _ in range(num_test_cases):
            s = f.readline().strip()
            test_case = TestCase(s)
            test_cases.append(test_case)
    return num_test_cases, test_cases

if __name__ == "__main__":
    num_test_cases, test_cases = read_data("A-large.in")
    for it in range(num_test_cases):
        test_case = test_cases[it]
        print("Case #{}:".format(it + 1), test_case.solve())