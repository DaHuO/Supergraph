import sys
def solve_all(cases):
    # Solve each case
    for case in cases:
        counter = 1
        seen = set()
        while True:
            # Determine if infinite
            if case == 0:
                yield "INSOMNIA"
                break

            name = counter * case
            seen.update([int(x) for x in str(name)])
            if all(x in seen for x in (range(10))):
                yield name
                break

            counter += 1

if __name__ == "__main__":
    path = sys.argv[1]
    num_cases = None
    cases = []

    # Get cases
    with open(path, 'r') as f:
        num_cases = int(f.readline().strip())
        for x in range(num_cases):
            cases.append(int(f.readline().strip()))

    gen = solve_all(cases)
    for x in range(num_cases):
        print "Case #%s: %s" % (x+1, gen.next())