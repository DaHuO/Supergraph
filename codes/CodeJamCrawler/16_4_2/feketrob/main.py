__author__ = 'Roberto'
import math
from itertools import combinations

def finish(index, solution):

    print solution

    file_out.write("Case #{0}: {1}\n".format(index+1, solution))

def solve_test(index, test_case):

    print "Case: [{0}]".format(test_case)

    N, K = map(int, test_case[0].split())
    Ps = map(float, test_case[1].split())
    #print N, K, Ps

    max_p = 0
    for c  in combinations(Ps, K):

        total = 0
        for c2 in combinations(c, K/2):
            others = list(c)
            for e in c2: others.remove(e)

            temp = 1 - c2[0]
            for i in xrange(1, len(c2)):
                temp *= (1 - c2[i])
            for e in others:
                temp *= e

            total += temp

        if total > max_p:
            max_p = total

    finish(index, max_p)


task = "B"
level = 1
attempts = 0

if level == 0:
    file_name = "sample.in"
elif level == 1:
    file_name = "{0}-small-attempt{1}.in".format(task, attempts)
else:
    file_name = "{0}-large-attempt.in".format(task)



file_out_name = file_name.replace("in", "out")
file_out = open(file_out_name, 'w')

with open(file_name, 'r') as file:
    content = file.read()

lines = content.split('\n')
number_of_lines = int(lines[0])

test_cases = lines[1:]

for i in xrange(0, number_of_lines):


    solve_test(i, test_cases[i*2:i*2+2])

file_out.close()