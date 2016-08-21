"""
Problem B

@author: Krisztian Balog
"""

import sys


class Solver(object):
    def __init__(self):
        self.flips = {}

    @staticmethod
    def flip(s):
        s2 = ""
        for c in s:
            s2 += "-" if c == "+" else "+"
        return s2

    def solve(self, s):
        """Classic dynamic programming."""
        if s not in self.flips:  # if it has not already been computed
            n = len(s)
            allp = n * "+"
            if s == allp:  # all +: no flips needed
                self.flips[s] = 0
            elif s == n * "-":  # all -: 1 flip needed
                self.flips[s] = 1
            else:  # contains both + and -
                for i in range(n):
                    top = self.flip(s[0:i + 1])  # top of the stack (flipped)
                    bottom = s[i + 1:n + 1]  # bottom of the stack
                    f2 = 1 + self.solve(top) + self.solve(bottom)  # #flips needed
                    if s not in self.flips or f2 < self.flips[s]:
                        self.flips[s] = f2
                    # print(str(i) + ": " + s + " => " + top + "  |  " + bottom + "  (" + str(f2) + ") ")
        return self.flips[s]


def run(infile, outfile):
    with open(infile, "r") as f:
        t = int(f.readline().strip())
        cases = [f.readline().strip() for i in range(t)]
    solver = Solver()
    with open(outfile, "w") as f:
        for i, s in enumerate(cases):
            f.write("Case #" + str(i + 1) + ": " + str(solver.solve(s)) + "\n")


if __name__ == "__main__":
    run("B-large.in", "B-large.out")
