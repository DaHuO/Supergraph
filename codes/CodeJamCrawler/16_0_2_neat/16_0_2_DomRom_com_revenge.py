
def f(n):
    n = str(n[::-1])
    current = "-"
    count = 0
    ind = 0
    i = n.find(current, ind)
    ind = i
    while i != -1:
        count += 1

        if current == "-":
            current = "+"
        else:
            current = "-"

        i = n.find(current, ind)
        ind = i

    return count


testcase = file("testcase.in", "r")
x = []
for line in testcase:
    x.append(line.strip())

outfile = file("testcase.out", "w")
print x
for i in xrange(1,len(x)):
    pancakes = x[i]
    print pancakes
    outfile.write("Case #%s: %s\n"%(i, f(pancakes)))

outfile.close()
