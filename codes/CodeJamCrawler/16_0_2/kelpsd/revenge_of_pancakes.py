import sys

def count_flips(stack: str) -> int:
    partitions = 0
    face = stack[0]
    for p in stack:
        if p != face:
            partitions += 1
            face = p

    if face == '-':
        return partitions + 1
    else:
        return partitions


assert(count_flips("-") == 1)
assert(count_flips("-+") == 1)
assert(count_flips("+-") == 2)
assert(count_flips("+++") == 0)
assert(count_flips("--+-") == 3)
assert(count_flips("+++++++++++++") == 0)
assert(count_flips("++++++-+++++++") == 2)
assert(count_flips("-+-+-+-+") == 7)

t = int(sys.stdin.readline())
for i in range(0, t):
    stack = sys.stdin.readline().strip()
    print("Case #%d: %s" % (i+1, count_flips(stack)))

