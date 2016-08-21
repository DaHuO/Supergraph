
def solve(inp):
    if inp == '0':
        return "INSOMNIA"

    seen = {}

    for i in range(1, 10000000):
        last = str(int(inp) * i)
        for c in last:
            seen[c] = 1

        if len(seen) == 10:
            return last

    return "INSOMNIA"

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
