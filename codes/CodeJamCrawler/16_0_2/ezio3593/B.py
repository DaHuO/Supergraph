def split_stack(stack):
    last_elem = stack[-1]
    split_index = -1
    for i in xrange(len(stack) - 2, -1, -1):
        if stack[i] == last_elem:
            split_index -= 1
        else:
            break
    return stack[:split_index], stack[split_index:]


def get_answer(stack, change_to_happy=True):
    if change_to_happy:
        if 0 not in stack:
            return 0

        if 1 not in stack:
            return 1
    else:
        if 0 not in stack:
            return 1

        if 1 not in stack:
            return 0

    first, second = split_stack(stack)
    # first.reverse()
    if change_to_happy:
        if second[0] == 1:
            return get_answer(first)
        else:
            return 1 + get_answer(first, False)
    else:
        if second[0] == 1:
            return 1 + get_answer(first)
        else:
            return get_answer(first, False)


out = open('out.txt', 'w')

with open("B-large.in") as f:
    data = f.read().split('\n')
    t = int(data[0])
    for i in xrange(1, t + 1):
        tmp_data = [1 if c == '+' else 0 for c in data[i]]
        out.write("Case #{}: {}\n".format(i, get_answer(tmp_data)))

out.close()
