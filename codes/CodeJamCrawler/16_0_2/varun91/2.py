count = int(input())

def solve(input, pos, steps=[]):
    if pos == 0:
        return 0
    if input[pos-1] == '+':
        return solve(input, pos-1, steps)
    for i in range(pos):
        input[i] = '+' if input[i] == '-' else '-'
    steps.append(1)
    return solve(input, pos-1, steps)

for i in range(count):
    str = input()
    steps = []
    solve(list(str), len(str), steps)
    print("Case #%d: %d" % (i+1,len(steps)))
