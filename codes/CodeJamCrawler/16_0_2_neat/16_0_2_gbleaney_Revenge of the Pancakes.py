input = open('./B-large.in', 'r')
output = open('./B-large.out', 'w')

def writeOut(i, out):
    output.write("Case #" + str(i) + ": " + str(out) + "\n")

tests = int(input.readline())

def flip(s, i):
    top = s[0:i]
    reversed = top[::-1]
    flipped = "".join(["+" if c == "-" else "-" for c in reversed])
    remainder = s[i:]
    return flipped + remainder

for i in range(1, tests+1):
    stack = input.readline()

    print '\n'
    print stack

    flips = 0

    while "-" in stack:
        if stack[0] == "+":
            neg = stack.find("-")
            stack = flip(stack, neg)

        else:
            neg = stack.rfind("-") + 1
            stack = flip(stack, neg)

        print stack
        flips += 1

    writeOut(i, flips)


