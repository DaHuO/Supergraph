import sys


DEBUG=True if len(sys.argv) > 1 else False


def debug(*texts):
    if DEBUG:
        print("[DEBUG]", *texts, flush=True)



def solve(number):
    if number == 0:
        return "INSOMNIA"
    seen = set()
    last = number
    i = 0
    while True:
        i += 1
        last = i * number
        seen |= set([c for c in str(i * number)])
        debug(last, seen)
        if len(seen) == 10:
            return str(last)


for case in range(1, int(sys.stdin.readline())+1):
    number = int(sys.stdin.readline())

    debug("number:", number)

    solution = solve(number)

    print("Case #{0}: {1}".format(case, solution))

