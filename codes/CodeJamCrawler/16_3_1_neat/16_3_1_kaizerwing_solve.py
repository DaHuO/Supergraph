def num_pair(pairs):
    count = 0
    for p in pairs:
        count += p[0]
    return count

for t in range(int(input().strip())):
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    pairs = []
    for idx, e in enumerate(nums):
        pair = [e, chr(ord('A') + idx)]
        pairs.append(pair)

    print("Case #%d:" % (t + 1), end="")
    np = num_pair(pairs)
    while np > 0:
        pairs.sort(key = lambda x: x[0], reverse = True)
        if np == 3:
            print(" %s" % pairs[0][1], end="")
            pairs[0][0] -= 1
        elif pairs[0][0] == pairs[1][0]:
            print(" %s%s" % (pairs[0][1], pairs[1][1]), end="")
            pairs[0][0] -= 1
            pairs[1][0] -= 1
        else:
            print(" %s%s" % (pairs[0][1], pairs[0][1]), end="")
            pairs[0][0] -= 2
        np = num_pair(pairs)
    print("")
