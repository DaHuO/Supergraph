HAPPY_SIDE = '+'
BLANK_SIDE = '-'

def are_happy_sided(pancakes):
    for pancake in pancakes:
        if pancake == BLANK_SIDE:
            return False
    return True

def number_of_pancakes_at_front(pancakes, side):
    i = 0
    while i < len(pancakes) and pancakes[i] == side:
        i += 1
    return i


def flip(pancakes):
    pancakes = pancakes.rstrip(HAPPY_SIDE)
    if number_of_pancakes_at_front(pancakes, BLANK_SIDE) > 0:
        pancakes = pancakes.lstrip(BLANK_SIDE)
    else:
        happy_sided_at_front = number_of_pancakes_at_front(pancakes, HAPPY_SIDE)
        pancakes = (BLANK_SIDE * happy_sided_at_front) + pancakes.lstrip(HAPPY_SIDE)
    return pancakes

def min_flips_to_get_happy_side(pancakes):
    flips = 0
    while not are_happy_sided(pancakes):
        pancakes = flip(pancakes)
        flips += 1
    return flips


T = int(input())
for t in range(1, T + 1):
    pancakes = input().strip()
    print('Case #{}: {}'.format(t, min_flips_to_get_happy_side(pancakes)))