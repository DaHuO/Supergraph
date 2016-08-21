from collections import defaultdict


t = int(raw_input())
test_cases = defaultdict(set)


def flip_stack(stack):
    return ''.join(
        ["+" if pancake == "-" else "-" for pancake in stack]
    )


for x in xrange(1, t + 1):
    stack = raw_input()
    loops = 0
    while "-" in stack:
        loops += 1
        if len(stack) == 1:
            break
        flip_index = stack.rfind("-")
        flip_these = stack[:flip_index + 1]
        keep_these = stack[flip_index + 1:]
        stack = ''.join([flip_stack(flip_these), keep_these])
    print("Case #%d: %d" % (x, loops))
