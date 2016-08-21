__author__ = 'Roberto'
import math

def finish(index, solution):

    print solution

    file_out.write("Case #{0}: {1}\n".format(index+1, solution))

def solve_test(index, test_case):

    print "Case: [{0}]".format(test_case)

    K, C, S = map(int, test_case.split(" "))
    if K == 1:
        finish(index, "1")
        return

    if C == 1:
        if K > S:
            finish(index, "IMPOSSIBLE")
            return
        else:
            finish(index, " ".join([str(i + 1) for i in xrange(K)]))
            return

    if K == 2:
        finish(index, "2")
        return

    cleanings = []
    for i in xrange(K):
        position = 1
        for j in xrange(C):
            position += i * pow(K, j)

        cleanings.append(position)

    # if K < C:
    #     position = 1
    #     for i in xrange(K):
    #         position += pow(K, K-i-1) * i
    #
    #     finish(index, position)
    #     return
    #
    # no_solution = int(math.ceil(float(K)/C))
    # if no_solution > S:
    #     finish(index, "IMPOSSIBLE")
    #
    # cleanings = []
    #
    # if C < K and K % C != 0:
    #     cleanings.append(int(pow(K, C)))
    #
    # offset = 0
    # while len(cleanings) < no_solution:
    #
    #     position = 1
    #     for i in xrange(C):
    #         position += pow(K, C-i-1) * (i + offset)
    #
    #     cleanings.append(position)
    #     offset += C

    finish(index, " ".join(map(str, cleanings)))


task = "D"
level = 1
attempts = 7

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