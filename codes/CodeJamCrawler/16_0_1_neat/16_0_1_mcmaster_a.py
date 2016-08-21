"""
Problem A

@author: Krisztian Balog
"""


def visit(n, visited):
    """Marks all digits of the number n visited and returns the total number of digits visited so far"""
    for c in str(n):
        visited[int(c)] = 1
    return sum(visited.values())


def solve(n):
    # It will always terminate, except when n=0
    if n == 0:
        return "INSOMNIA"

    visited = {i: 0 for i in range(10)}  # holds whether that number vas visited
    s = visit(n, visited)
    i = 1

    while s != 10:
        i += 1
        s = visit(i * n, visited)

    return str(i * n)  # last number seen


def run(infile, outfile):
    with open(infile, "r") as f:
        t = int(f.readline().strip())
        cases = [int(f.readline().strip()) for i in range(t)]
    with open(outfile, "w") as f:
        for i, n in enumerate(cases):
            sol = solve(n)
            print(sol)
            f.write("Case #" + str(i + 1) + ": " + sol + "\n")


if __name__ == "__main__":
    run("A-large.in", "A-large.out")