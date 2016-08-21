import string

file_in = "pancakes.in"
file_out = "pancakes.out"

def inv(c):
    if c == '+':
        return '-'
    else:
        return '+'

def flip(stack, n):
    head = stack[:n]
    tail = stack[n:]

    new_head = ""
    for c in reversed(head):
        new_head = new_head + inv(c)

    return new_head + tail


def solve(stack, ch):
    if len(stack) == 1:
        if stack == ch: return 0
        else: return 1

    if stack[-1] == ch:
        return solve(stack[:-1], ch)
    else:
        return 1 + solve(stack[:-1], inv(ch))


with open(file_in) as fin, open(file_out, "w") as fout:
    T = int(fin.readline())

    for i in range(T):
        stack = fin.readline()

        answer = solve(stack.rstrip(), '+')
        
        print("Case #{}: {}".format(i+1, answer), file=fout)

