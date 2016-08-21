file = open('B-large.in')
out = open('output.in', 'w')
T = int(file.readline().strip())
case = 1
for cases in range(T):
    s = file.readline().splitlines()[0]

    stack = []
    for p in s:
        if p == '+':
            stack.append(True)
        else:
            stack.append(False)

    first_pancake = stack[0]

    flips = 0
    for p in stack[1:]:
        if p != first_pancake:
            flips += 1
            first_pancake = p

    if not stack[-1]:
        flips += 1

    out.write("Case #%i: %s\n" % (case, flips))
    case += 1
