def flip(stack, i):
    flipped = [x ^ 1 for x in stack[0:i+1]][::-1]
    stack = flipped + stack[i+1:]
    return stack

cases = int(raw_input().strip())
out = open('output.txt', 'w')

for case in range(cases):
    flips = 0
    stack = [1 if x == '+' else 0 for x in raw_input().strip()]
    print stack

    while 0 in stack:
        if 1 not in stack:
            stack = flip(stack, len(stack)-1)
            flips += 1
            continue
        firstsad = stack.index(0)
        lastsad = len(stack)-stack[::-1].index(0)-1
        firsthappy = stack.index(1)

        if firsthappy < firstsad:
            stack = flip(stack, firstsad-1)
            flips += 1
        else:
            stack = flip(stack, lastsad)
            flips += 1

    s = "Case #"+str(case+1)+": "+str(flips)+'\n'
    out.write(s)
    print(s)
