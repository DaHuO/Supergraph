with open('in.txt') as f:
    lines = f.readlines()
lines = [l.split('\n')[0] for l in lines]
t = int(lines[0])


def flip(stack, split_point, n_pos, n_neg):
    new_stack = []
    new_n_pos, new_n_neg = n_pos, n_neg
    for i in xrange(split_point + 1):
        if stack[i] == '+':
            new_stack.append('-')
            new_n_neg += 1
            new_n_pos -= 1
        else:
            new_stack.append('+')
            new_n_neg -= 1
            new_n_pos += 1
    new_stack = new_stack[::-1]
    new_stack.extend(stack[split_point + 1:])
    return new_stack, new_n_pos, new_n_neg


def count_pancakes(stack):
    n_neg, n_pos, n_total = 0, 0, 0
    for s in stack:
        if s == '-':
            n_neg += 1
        else:
            n_pos += 1
        n_total += 1

    n_flips = 0

    while True:
        if n_pos == n_total:
            return n_flips
        if n_neg == n_total:
            return n_flips + 1

        for i in xrange(n_total - 1):
            if stack[i] != stack[i + 1]:
                stack, n_pos, n_neg = flip(stack, i, n_pos, n_neg)
                n_flips += 1
            else:
                continue


f = open('out.txt', 'w')
for i in xrange(1, t + 1):
    stack = lines[i]
    ans = count_pancakes(stack)
    f.write('Case #%s: %s \n' % (i, ans))
f.close()
