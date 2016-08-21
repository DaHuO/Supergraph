
def flip_pie(pie):
    """@todo: Docstring for flip_pie.

    :pie: @todo
    :returns: @todo

    """
    if pie == "-":
        return "+"
    return "-"


def flip_stack(stack, pos=None):
    """flips the given stack

    :stack: @todo
    :returns: @todo

    """
    if pos == None:
        move_stack = [flip_pie(x) for x in stack]
    else:
        move_stack = [flip_pie(x) for x in stack[:pos + 1]]
    move_stack.reverse()
    new_stack = move_stack + list(stack[pos + 1:])
    return ''.join(new_stack)


def flip_left_most(stack, go_forth=False):
    """@todo: Docstring for flip_left_most.

    :stack: @todo
    :returns: @todo

    """
    start = stack[0]
    pos = 0
    for i in stack:
        if i != start:
            break
        pos += 1
    if len(stack) < 3 or pos > 1 or go_forth == True:
        return flip_stack(stack, pos - 1)
    return stack

def all_happy(stack):
    """@todo: Docstring for all_happy.

    :stack: @todo
    :returns: @todo

    """
    return stack.count('+') == len(stack)


def flipty_do(stack):
    moves = 0
    if all_happy(stack):
        return moves
    go_forth = False
    while True:
        new_stack = flip_left_most(stack, go_forth)
        if new_stack != stack:
            moves += 1
            go_forth = False
            stack = new_stack
            if all_happy(new_stack):
                return moves
        else:
            go_forth = True
    return moves


def main():
    """
    main
    """
    how_many = int(input())
    for i in range(1, how_many + 1):
        line = input()
        rep = flipty_do(line)
        print("Case #%s: %s" % (i, rep))


def test():
    """do some testing
    :returns: @todo

    """
    print("#1. %s = 1" % flipty_do("-"))
    print("#2. %s = 1" % flipty_do("-+"))
    print("#3. %s = 2" % flipty_do("+-"))
    print("#4. %s = 0" % flipty_do("+++"))
    print("#5. %s = 3" % flipty_do("--+-"))
    print("#6. %s = 3" % flipty_do("--+--+-"))
    print("#7. %s = 2" % flipty_do("+++---++++"))
    print("#8. %s = 4" % flipty_do("++++++--+-"))
    print("#9. %s = 1" % flipty_do("--++--+++--+-"))

if __name__ == '__main__':
    main()
