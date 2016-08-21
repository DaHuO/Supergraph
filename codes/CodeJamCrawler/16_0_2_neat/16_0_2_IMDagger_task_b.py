
def solve(mem, state, i, s):
    if (i, s) in mem:
        return mem[i, s]

    if i == 0:
        if state[i] == s:
            return 0
        else:
            return 1

    if state[i] == s:
        answer = solve(mem, state, i - 1, s)
    else:
        answer = min(
            solve(mem, state, i - 1, s) + 2,
            solve(mem, state, i - 1, not s) + 1
        )

    mem[i, s] = answer
    return answer


def pancakes_state(pancakes):
    return [(c == '+') for c in pancakes]


tests_count = int(raw_input())
for i in xrange(1, tests_count + 1):
    pancakes = raw_input().strip()
    sides = pancakes_state(pancakes)
    N = len(pancakes) - 1
    ops = min(
        solve({}, sides, N, True),
        solve({}, sides, N, False) + 1
    )
    print 'Case #{0}: {1}'.format(i, ops)
