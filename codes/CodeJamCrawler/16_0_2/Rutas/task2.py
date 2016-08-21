def go(stack):
    backward_stack = []
    for pan in stack[::-1]:
        if pan == '-':
            backward_stack.append(False)
        else:
            backward_stack.append(True)
    cnt = 0
    while not all(pan for pan in backward_stack):
        numbering = 0
        for pan in backward_stack:
            numbering += 1
            if not pan:
                backward_stack[numbering - 1:] = [not x for x in backward_stack[numbering - 1:]]
                cnt += 1
                break
    return cnt

t = int(input())
for i in range(1, t + 1):
    boo = input()
    answer = go(boo)
    print("Case #{}: {}".format(i, answer))
