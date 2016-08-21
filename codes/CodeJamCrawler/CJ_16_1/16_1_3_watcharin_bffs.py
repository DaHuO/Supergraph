import sys

def explore(n, f, original_path, excluded):
    rv = len(original_path)

    for i in range(n):
        if i in excluded:
            continue

        path = original_path[:]
        nxt = i

        while not nxt in path:
            path.append(nxt)

            nxt = f[nxt]

        if len(path) >= 2 and nxt == path[-2]:
            rv = max(rv, explore(n, f, path[:], [nxt]))
        elif nxt == path[0]:
            rv = max(rv, len(path))

    return rv

def solve(case, n, f):
    # TODO Solve the problem

    return str(explore(n, f, [ ], []))

### Convert the input file into a list of strings ###
in_file = sys.argv[1]

with open(in_file, "r") as f:
    data = f.read()

lines = data.splitlines()
### Convert the input file into a list of strings ###

### Interpret the arguments ###
cases = int(lines.pop(0))

for i in range(1, cases + 1):
    n = int(lines.pop(0))

    f = lines.pop(0).split()
    f = [ int(x) - 1 for x in f ]

    answer = solve(i, n, f)

    print 'Case #%d: %s' % (i, answer)
### Interpret the arguments ###
