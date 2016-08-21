def all_seen(seen):
    for s in seen:
        if not s:
            return False
    return True


tests = int(input())
seen = []
for i in range(1, tests + 1):
    n = int(input())
    cur = 0
    seen = [False] * 10
    if n == 0:
        print("Case #%s: %s" % (i, "INSOMNIA"))
    else:
        while not all_seen(seen):
            cur = n + cur
            for x in str(cur):
                seen[int(x)] = True
        print("Case #%s: %s" % (i, cur))

