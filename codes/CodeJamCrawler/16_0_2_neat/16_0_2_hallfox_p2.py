def flip(p):
    new_p = ""
    for c in p:
        new_p += "+" if c == "-" else "-"
    return new_p[::-1]


def solve(n):
    stack = n[:n.rfind('-')+1]
    n_flips = 0
    while '-' in stack:
        if stack[0] == '-':
            stack = flip(stack)
            stack = stack[:stack.rfind('-')+1]
        else:
            flip_point = stack.find('-')
            stack = flip(stack[:flip_point]) + stack[flip_point:]
        n_flips += 1
        # print(stack)
    return n_flips


n = int(input())
for i in range(n):
    print("Case #{}: {}".format(i+1, solve(input())))
