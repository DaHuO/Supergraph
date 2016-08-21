
def all_happy(pancakes):
    if '-' in pancakes:
        return False
    return True


def flip_pancakes(pancakes):
    flipped_pancakes = ''

    for s in pancakes:
        if s == '+':
            flipped_pancakes += '-'

        else:
            flipped_pancakes += '+'

    return flipped_pancakes


def pancake_maneuver(pancakes):
    pancakes = remove_fliped(pancakes)

    first_pancake = pancakes[0]

    if first_pancake == '-':
        return ''.join(reversed(flip_pancakes(pancakes)))

    else:
        last_happy_pancake = pancakes.rfind('+')
        sub_pancakes = pancakes[0:last_happy_pancake+1]

        return ''.join(reversed(flip_pancakes(sub_pancakes))) + pancakes[last_happy_pancake+1:]


def remove_fliped(pancakes):
    while len(pancakes) > 0 and pancakes[-1] == '+':
        pancakes = pancakes[:-1]

    return pancakes


for i in range(int(raw_input())):
    pancakes = raw_input()
    cnt = 0
    while not all_happy(pancakes):
        pancakes = pancake_maneuver(pancakes)
        cnt += 1
    print 'Case #%d: %d' % (i+1, cnt)