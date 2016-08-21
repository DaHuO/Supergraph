import sys

def solve(base_nb): # TODO
    nb = base_nb
    l = {i:i for i in range(0, 10)}
    i = 0
    limit = 100
    while i < limit:
        i += 1
        for digit in str(nb):
            if int(digit) in l:
                del l[int(digit)]
                if l == {}:
                    return nb
        nb += base_nb
    return "INSOMNIA"

# Parsing and functions call:
if __name__ == "__main__":
    tests = int(input())
    #print("{0} test(s) found.".format(tests), file=sys.stderr)
    for i in range(tests):
        result = solve(int(input()))
        print("Case #{0}: {1}".format(i+1, result))
    #print("Done.", file=sys.stderr)

