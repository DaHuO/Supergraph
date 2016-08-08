__author__ = 'Roberto'
import math
from itertools import permutations

def finish(index, solution):

    print solution

    file_out.write("Case #{0}: {1}\n".format(index+1, solution))

def test_p(p):

    if len(p) == 1:
        return True

    operations = {}
    operations[("R", "R")] = None
    operations[("R", "P")] = operations[("P", "R")] = "P"
    operations[("R", "S")] = operations[("S", "R")] = "R"
    operations[("S", "S")] = None
    operations[("S", "P")] = operations[("P", "S")] = "S"
    operations[("P", "P")] = None

    next_p = ""
    i = 0
    while i < len(p):
        next_c = operations[(p[i], p[i+1])]
        if next_c == None:
            return False
        next_p+=next_c
        i += 2

    return test_p(next_p)

def solve_test(index, test_case):

    print "Case: [{0}]".format(test_case)

    N, R, P, S = map(int, test_case.split())
    letters = []
    letters.extend(["R"] * R)
    letters.extend(["P"] * P)
    letters.extend(["S"] * S)

    for p in sorted(permutations(letters)):
        if test_p(p):
            finish(index, "".join(p))
            return

    finish(index, "IMPOSSIBLE")


task = "A"
level = 1
attempts = 0

if level == 0:
    file_name = "sample.in"
elif level == 1:
    file_name = "{0}-small-attempt{1}.in".format(task, attempts)
else:
    file_name = "{0}-large.in".format(task)



file_out_name = file_name.replace("in", "out")
file_out = open(file_out_name, 'w')

with open(file_name, 'r') as file:
    content = file.read()

lines = content.split('\n')
number_of_lines = int(lines[0])

test_cases = lines[1:]

for i in xrange(0, number_of_lines):

    solve_test(i, test_cases[i])

file_out.close()