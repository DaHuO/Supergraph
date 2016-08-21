def flip_upto(stack, sign):
    for i in range (1, len(stack)):
        if stack[i] != sign:
            return i

def flip(stack, index):
    part_to_flip = stack[:index]
    flipped_part = []
    for c in part_to_flip:
        if c == '+' :
            flipped_part.append('-')
        else:
            flipped_part.append('+')
    return ''.join(flipped_part[::-1]) + stack[index:]

def solve_stack(stack, sign, opposite_sign):
    moves = 0
    index = len(stack) - 1
    while index >= 0 :
        if stack[index] != sign:
            if stack[0] == opposite_sign:
                stack = flip(stack, index+1)
                index -= 1
            else :
                stack = flip(stack, flip_upto(stack, sign))
            moves += 1
        else :
            index -= 1
    return moves


def solve(stack):
    plus = solve_stack(stack, '+', '-')
    minus = solve_stack(stack, '-', '+') + 1
    return plus if plus < minus else minus
f = open('problem_b.txt', 'w')
cases = int(raw_input())
for i in range (1, cases+1):
    f.write("Case #" + str(i) + ": " + str(solve(raw_input())) + "\n")
f.close()