import fileinput


def solve(inp):
    if inp == 0:
        return "INSOMNIA"
    nums = set()
    n = 1
    while True:
        num = inp*n
        n += 1
        for c in str(num):
            nums.add(c)
        if len(nums) == 10:
            return num

for i, line in enumerate(fileinput.input()):
    if i == 0:
        continue
    line = int(line.strip())
    res = solve(line)
    print "Case #%d: %s" % (i, res)
