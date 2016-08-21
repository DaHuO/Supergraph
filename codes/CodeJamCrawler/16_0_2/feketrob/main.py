__author__ = 'Roberto'

def finish(index, solution):

    print solution

    file_out.write("Case #{0}: {1}\n".format(index+1, solution))

def solve_test(index, test_case):

    print "Case: [{0}]".format(test_case)

    no_steps = 0
    if test_case[0] == "-":
        no_steps += 1

    prev = ""
    for pancake in test_case:

        if prev == "+" and pancake == "-":
            no_steps +=2

        prev = pancake

    finish(index, no_steps)


task = "B"
level = 2

if level == 0:
    file_name = "sample.in"
elif level == 1:
    file_name = "{0}-small-attempt0.in".format(task)
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