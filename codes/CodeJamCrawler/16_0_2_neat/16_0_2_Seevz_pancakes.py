def flip(pancakes):
    pancakes.reverse()
    for i in range(len(pancakes)):
        if pancakes[i] == "+":
            pancakes[i] = "-"
        else:
            pancakes[i] = "+"

    return pancakes

for x in range(int(input())):
    stack = list(input())
    counter = 0

    while "-" in stack:
        while stack[-1] == "+":
            stack.pop()

        i = 0
        while stack[i] == "+":
            i += 1

        if i == 0:
            stack = flip(stack)
        else:
            stack[0:i] = flip(stack[0:i])

        counter += 1

    print("Case #%d: %d" % (x+1, counter))
