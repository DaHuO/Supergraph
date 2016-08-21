def func(S):
    stack = []
    alreadyDone = []
    end = ['+'] * len(S)

    for sign in S:
        stack.append(sign)

    queue = [[stack, 0]]

    if stack == end:
        return 0

    while queue is not []:
        current = queue.pop(0)
        currentStack = current[0]
        currentNum = current[1]

        if currentStack == end:
            return currentNum

        for n in range(1, len(S) + 1):
            newStack = flip(currentStack, n)

            if newStack not in alreadyDone:
                queue.append([flip(currentStack, n), (currentNum + 1)])
                alreadyDone.append(newStack)


def flip(stack, N):
    flipping = []
    flipped = []

    for i in range(len(stack)):
        if i < N:
            flipping.append(stack[i])
        flipped.append(stack[i])

    flipping.reverse()

    for i in range(len(flipping)):
        if flipping[i] == '+':
            flipping[i] = '-'
        else:
            flipping[i] = '+'

    flipped[:N] = flipping

    return flipped

T = int(input())

for t in range(T):
    S = input()
    print('Case #' + str(t+1) + ': ' + str(func(S)))
