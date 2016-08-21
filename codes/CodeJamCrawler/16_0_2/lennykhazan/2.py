T = int(input())

def flip(stack, idx):
    ref = stack[:idx+1]
    seg = stack[:idx+1]
    for i in range(len(seg)):
        if ref[idx-i] == '-':
            seg[i] = '+'
        else:
            seg[i] = '-'
    stack[:idx+1] = seg
    return stack

def completed(stack):
    for i in stack:
        if i != '+':
            return False

    return True

def solve(stack):
    stack = list(stack)
    idx = len(stack)-1

    moves = 0
    while not completed(stack):
        while stack[idx] == '+':
            idx -= 1

        if stack[0] == '-':
            stack = flip(stack, idx)
            moves += 1
            
        else:
            idx2 = idx
            while stack[idx2] == '-':
                idx2 -= 1
            stack = flip(stack, idx2)
            moves += 1

    return moves

for t in range(T):
    print('Case #' + str(t+1) + ': ' + str(solve(input())))
