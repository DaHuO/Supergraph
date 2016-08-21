
def f(n):
    if n == 0:
        return "INSOMNIA"
    x = n
    seen = set()
    while len(seen) < 10:
        for i in str(x):
            if i not in seen:
                seen.add(i)
        x += n
    return x-n


testcase = file("testcase.in", "r")
x = []
for line in testcase:
    x.append(int(line.strip()))

outfile = file("testcase.out", "w")

for i in xrange(len(x)-1):
    number = int(x[i+1])
    outfile.write("Case #%s: %s\n"%(i+1, f(number)))

outfile.close()
