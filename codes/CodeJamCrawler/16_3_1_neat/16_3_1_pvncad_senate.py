import sys

T = int(raw_input())
for tc in xrange(1, T + 1):
    N = int(raw_input())
    nums = [[chr(ord('A') + i), int(w)] for i, w in enumerate(raw_input().split())]

    nums = sorted(nums, key=lambda x: x[1])

    evacuted = 0

    curr = 0
    maj = nums[-1][1]

    sol = []

    P = sum([r[1] for r in nums])

    while (P - evacuted) >= (maj * 2 + 2):
        nums[curr][1] -= 1
        out = nums[curr][0]

        if nums[curr][1] == 0:
            curr += 1

        nums[curr][1] -= 1
        out +=  nums[curr][0]

        if nums[curr][1] == 0:
            curr += 1
        sol.append(out)

        evacuted += 2

    if maj * 2 < (P - evacuted):
        sol.append(nums[curr][0])
        nums[curr][1] -= 1

        if nums[curr][1] == 0:
            curr += 1
        evacuted += 1

    while evacuted < P:
        out = nums[-1][0]
        out +=  nums[curr][0]

        nums[curr][1] -= 1

        if nums[curr][1] == 0:
            curr += 1

        sol.append(out)
        evacuted += 2

    print "Case #%d: %s" % (tc, " ".join(sol))

