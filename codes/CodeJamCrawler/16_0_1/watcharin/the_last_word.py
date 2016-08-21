import sys

def solve(case, s):
    # TODO Solve the problem
    cur = ""

    for c in s:
        choices = [ cur + c, c + cur ]
        choices.sort()

        cur = choices[1]

    return cur

### Convert the input file into a list of strings ###
in_file = sys.argv[1]

with open(in_file, "r") as f:
    data = f.read()

lines = data.splitlines()
### Convert the input file into a list of strings ###

### Interpret the arguments ###
cases = int(lines.pop(0))

for i in range(1, cases + 1):
    s = lines.pop(0)

    answer = solve(i, s)

    print 'Case #%d: %s' % (i, answer)
### Interpret the arguments ###
