lines = [line.rstrip() for line in open('input-small.in')]

def flip(stack):
    return ['+' if x=='-' else '-' for x in stack[::-1]]

def solve(stack, count, ex):
    expe = [ex] * len(stack)
    if(stack == expe):
        return count

    if(stack[-1] == '+'):
        x = solve(stack[:-1], count, '+')
        y = solve(flip(stack[:-1]), count+1, '+')
        ans = min(x, y)
        if ex != '+':
            ans = ans + 1
        return ans

    if(stack[-1] == '-'):
        x = solve(stack[:-1], count, '-')
        y = solve(flip(stack[:-1]), count+1, '-')
        ans = min(x, y)
        if ex != '-':
            ans = ans + 1
        return ans

for i in range(int(lines[0])):
    val = lines[i+1]
    ans = solve(list(val), 0, '+')

    print 'Case #%d: %s' % (i+1, ans)

