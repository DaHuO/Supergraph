def flip_pancakes(stack, inverted=False):
    want = '-' if inverted else '+'
    no_want = '+' if inverted else '-'
    locked_pancakes = 0
    for pancake in reversed(stack):
        if pancake != want:
            break
        locked_pancakes += 1
    else:
        return 0
    return 1 + flip_pancakes(stack[:-locked_pancakes-1], not inverted)

for case in range(int(input())):
    print("Case #{}: {}".format(
        case+1,
        flip_pancakes(input())
    ))
