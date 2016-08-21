import sys


DEBUG=True if len(sys.argv) > 1 else False

def debug(*texts):
    if DEBUG:
        print("[DEBUG]", *texts, flush=True)


def solve(stack):
    """
    ...++   s' = s (solve "...")
            t' = t (consider last consecutive '+' as one)

    ...-+   s' = s (solve "...-")
            t' <= min(s+1, t+2)

    ...+-   s' <= min(s+2, t+1)
            t' = t (solve "...+")

    ...--   s' = s (consider last consecutive '-' as one)
            t' = t (solve "...")
    """

    plus = 0 if stack[0] == '+' else 1
    minus = 0 if stack[0] == '-' else 1

    for i in range(2, len(stack)+1):
        s = stack[:i]
        last2 = ''.join(s[-2:])
        if last2 == '++' or last2 == '--':
            plus = plus
            minus = minus
        elif last2 == '-+':
            plus = plus
            minus = min(plus+1, minus+2)
        elif last2 == '+-':
            plus = min(plus+2, minus+1)
            minus = minus
        debug(s, "...", last2, "...", plus, "...", minus)

    return plus



for case in range(1, int(sys.stdin.readline())+1):
    stack = [c for c in sys.stdin.readline() if c != '\n']

    debug("stack:", stack)

    solution = solve(stack)

    print("Case #{0}: {1}".format(case, solution))

