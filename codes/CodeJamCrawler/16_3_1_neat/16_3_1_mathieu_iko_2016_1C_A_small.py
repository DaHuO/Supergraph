import sys



DEBUG=True if len(sys.argv) > 1 else False
def debug(*texts):
    if DEBUG:
        print("[DEBUG]", *texts, flush=True)



def solve(senators):
    sol = ""
    while True:
        r = sum(senators.values())
        if not r:
            break
        k = max(senators, key = senators.get)
        sol += chr(64 + k)
        senators[k] -= 1

        r = sum(senators.values())
        if not r:
            break
        k = max(senators, key = senators.get)
        senators[k] -= 1
        new_r = sum(senators.values())
        if new_r > 0 and max(senators, key = senators.get) > sum(senators.values())/2:
            senators[k] += 1
        else:
            sol += chr(64 + k)
        sol += " "
    return sol



for case in range(1, int(sys.stdin.readline())+1):
    _ = sys.stdin.readline()
    senators = dict(enumerate(map(int, sys.stdin.readline().split()), start=1))

    debug(senators)

    solution = solve(senators)

    print("Case #{0}: {1}".format(case, solution))

