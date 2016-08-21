t = int(input())

for i in range (1, t+1):
    stack = list(input()[::-1])
    if '\r' in stack:
        stack.remove('\r')
    count = 0
    for j in range(len(stack)):
        if j == 0:
            if stack[j] == '-':
                count += 1
            continue

        if stack[j-1] != stack[j]:
            count += 1

    print("Case #{}: {}".format(i, count))
