def resolve(line):
    return count_flips(encode(line), False)


def count_flips(stack, pos):
    if not stack:
        return 0
    else:
        if stack[-1] == pos:
            return count_flips(stack[:-1], pos)
        else:
            return count_flips(stack[:-1], not pos) + 1


def encode(line):
    return [p == '-' for p in line]


# Trash:

def decode(stack):
    return ''.join('-' if p else '+' for p in stack)


def full_flip(stack):
    stack.reverse()
    return [not p for p in stack]


def flip(stack, top_n):
    top = stack[:top_n]
    bottom = stack[top_n:]
    top = [not p for p in top]
    top.reverse()
    return top + bottom


# Handle IO


def main():
    get_line()  # dicard first

    line = get_line()
    i = 1
    while line:
        print 'Case #{}: {}'.format(i, resolve(line))
        line = get_line()
        i += 1


def debug(*args):
    print ' '.join(map(str, args))


def get_line():
    try:
        return raw_input()
    except EOFError:
        return None


if __name__ == '__main__':
    main()
