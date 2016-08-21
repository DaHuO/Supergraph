def flip(side):
    if side == '+':
        return '-'
    else:
        return '+'

def happyize(stack):
    moves = 0
    for i in range(len(stack)-1, -1, -1):
        if stack[i] == '-':
            if stack[0] == '+':
                k = 0
                while stack[k] == '+':
                    stack[k] = '-'
                    k += 1
                moves += 1
            for j in range((i+1)//2):
                stack[j], stack[i-j] = flip(stack[i-j]), flip(stack[j])
            if i%2 == 0:
                stack[(i+1)//2] = flip(stack[(i+1)//2])
            moves += 1
    return moves

if __name__ == "__main__":
    t = int(input())
    for i in range(1, t+1):
        stack = list(input())
        print("Case #{}: {}".format(i, happyize(stack)))
