def flip(stack, n):
    if n > 0:
        flipped_stack = stack[0:n]
        flipped_stack = flipped_stack[::-1]
        for i in range(n):
            stack[i] = flipped_stack[i]
    else:
        stack = stack[::-1]
        n = len(stack)
    for i in range(n):
        if stack[i] == '-':
            stack[i] = '+'
        else:
            stack[i] = '-'
    return stack

# x = ['+', '-', '-', '+', '+']
# print(x)
# x = flip(x, 3)
# print(x)

with open("B-large.in", "r") as fin, open("output.out", "w") as fout:
    T = int(fin.readline().strip())
    for case in range(T):
        stack = [p for p in fin.readline().strip()]
        flip_counter = 0
        while "-" in stack:
            for i in range(len(stack)-1):
                if stack[i] != stack[i+1]:
                    stack = flip(stack, i+1)
                    flip_counter += 1
            if stack[-1] == "-":
                stack = flip(stack, -1)
                flip_counter += 1

        fout.write("Case #{}: {}\n".format(case + 1, flip_counter))

    print("done")
