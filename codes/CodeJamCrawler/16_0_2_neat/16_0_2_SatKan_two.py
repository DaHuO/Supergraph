import sys

fp = open(sys.argv[1], "r")
output = open(sys.argv[2], "w")

total = int(fp.readline())

case = 0

for stack in fp:
    case = case + 1
    m = 0

    cakes = list(stack)
    if cakes[-1] == '\n':
        # remove last newline
        del cakes[-1]

    for i in range(1, len(cakes)):
        if cakes[i] != cakes[i-1]:
            m = m + 1

    if cakes[-1] == '-':
        m = m + 1

    output.write("Case #{}: {}\n".format(case, m))

fp.close()
output.close()
