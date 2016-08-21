f = open('A-large.in')
out = open('output.txt', 'w')
t = int(f.readline())
for i in range(t):
    curr = f.readline()
    n = int(curr)
    if n == 0:
        out.write("Case #{}: INSOMNIA\n".format(i+1))
        continue
    nums_seen = {}
    for j in range(len(curr)):
        nums_seen[curr[j]] = "foo"
    while len(nums_seen) <= 10:
        curr = str(int(curr) + n)
        for j in range(len(curr)):
            nums_seen[curr[j]] = "foo"
    out.write("Case #{}: {}\n".format(i+1, curr))
