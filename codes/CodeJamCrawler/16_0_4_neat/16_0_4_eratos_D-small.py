import fileinput, sys

def solve(k, c, s):
    ans = ""
    for i in range(0, k):
        ans += "%s " % (i + 1)
    return ans

index = 0
for line in fileinput.input():
    index += 1
    if index == 1:
        continue
    tokens = line.split(" ")
    k = int(tokens[0])
    c = int(tokens[1])
    s = int(tokens[2])
    print("Case #%d: %s" % (index - 1, solve(k, c, s)))
