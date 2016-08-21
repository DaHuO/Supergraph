def FlipPancake(pancake):
        return '-' if pancake == '+' else '+'

def FlipStack(stack, size):
    for i in range(0, size // 2):
        temp = stack[i]
        stack[i] = FlipPancake(stack[size - 1 - i])
        stack[size - 1 - i] =  FlipPancake(temp)

    if size % 2 != 0:
        index = size // 2
        stack[index] =  FlipPancake(stack[index])

def GetNumPancakeFlips(stack):
    size = len(stack)
    numFlips = 0

    while 1:
        type = stack[0]
        for i in range(0, size):
            if stack[i] != type:
                FlipStack(stack, i)
                numFlips += 1
                break;

            if i == size - 1:
                if type == '-':
                    FlipStack(stack, size)
                    numFlips += 1
                return numFlips;

numTests = int(raw_input())
for i in range(1, numTests + 1):
    stack = list(raw_input())
    numFlips = GetNumPancakeFlips(stack)
    print("Case #{}: {}".format(i, numFlips))
