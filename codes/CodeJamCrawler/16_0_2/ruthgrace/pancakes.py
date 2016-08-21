f = open('input.txt', 'r')

cases = int(f.readline())

for i in range(cases):
    stack = f.readline().strip()
    start = 0
    end = len(stack) - 1
    flips = 0;
    while (start <= end):
        while (end >= 0 and stack[end] == '+'):
            end = end - 1
        if (end < start):
            break
        if (stack[start] == '+'):
            while (start < len(stack) and stack[start] == '+'):
                start = start + 1
            flips = flips + 1
        while (start < len(stack) and stack[start] == '-'):
            start = start + 1
        flips = flips + 1
        if (start > end):
            break
        while (end >= 0 and stack[end] == '-'):
            end = end - 1
        flips = flips + 1
        if (start > end):
            break
        while (end >= 0 and stack[end] == '+'):
            end = end - 1
        flips = flips + 1
    print("Case #" + str(i+1) + ": " + str(flips))
