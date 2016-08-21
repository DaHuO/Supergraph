#! venv/bin/python3.4


def are_they_all_something(pancakes, symbol='+'):
    """
    This function returns True if all the pancakes are 'happy'.
    Basically it checks if all the items in an array are the same and if that
    one item is a '+'.
    """
    return len(set(pancakes)) == 1 and pancakes[0] == symbol


def flip_pancakes(pancakes, index):
    target = pancakes[:index]
    target = target[::-1]
    for i in range(index):
        pancakes[i] = '+' if target[i] == '-' else '-'


def count_flips(pancakes):
    if are_they_all_something(pancakes):
        return 0
    elif are_they_all_something(pancakes, symbol='-'):
        return 1
    else:
        flips = 0 if pancakes[-1] == '+' else 1
        current = pancakes[0]
        for i in range(1, len(pancakes)):
            if pancakes[i] != current:
                flips += 1
            current = pancakes[i]
        return flips


cases = int(input())
for case in range(cases):
    pancakes = list(input())
    print("Case #{}: {}".format(case + 1, count_flips(pancakes)))
