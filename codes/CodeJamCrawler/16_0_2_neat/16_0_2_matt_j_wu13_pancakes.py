t = int(input())

def solve(stack):
    simplifiedStack = ""
    for s in stack:
        if len(simplifiedStack) == 0 or simplifiedStack[-1] != s:
            simplifiedStack += s
    if simplifiedStack[-1] == "+":
        simplifiedStack = simplifiedStack[:len(simplifiedStack) - 1]
    return len(simplifiedStack)


for i in range(1, t + 1):
    stack = input()
    solution = solve(stack)
    print("Case #{}: {}".format(i, solution))
