def make_binary(stack):
    binary = []
    for char in stack:
        if char == '-':
            binary.append(0)
        else:
            binary.append(1)
    return binary


def get_count(binary_stack):
    count = 0
    last_char = binary_stack[0]
    for char in binary_stack:
        if char == last_char:
            continue
        count += 1
        last_char = char

    if last_char == 0:
        count += 1

    return count

t = input()
for case in range(0, t):
    stack = raw_input()
    binary_stack = make_binary(stack)
    count = get_count(binary_stack)
    print "Case #" + str(case+1) + ":", count



