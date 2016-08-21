def main():
    with open('B-large.in') as input_file, open('B-large.out', 'w') as output_file:
        case_count = int(input_file.readline().strip())
        for i in range(case_count):
            case_no = i + 1
            pancake_stack = [Pancake(p == '+') for p in input_file.readline().strip()]
            flips = get_minimum_flips(pancake_stack)
            output_file.write('Case #%d: %d\n' % (case_no, flips))


class Pancake(object):
    HAPPY = True
    BLANK = False

    def __init__(self, is_happy):
        self.is_happy = is_happy

    def flip(self):
        self.is_happy = not self.is_happy

    def __repr__(self):
        # for debug
        return '+' if self.is_happy else '-'


def get_minimum_flips(pancake_stack):
    flips = 0
    while True:
        flip_point = get_flip_point(pancake_stack)
        if flip_point is None:
            break
        for pancake in pancake_stack[:flip_point]:
            pancake.flip()
        flips += 1
    return flips


def get_flip_point(pancake_stack, start=0):
    if pancake_stack[start].is_happy:
        # when stack starts with happy pancake, change start point
        first_blank = find_pancake_index(pancake_stack, Pancake.BLANK)
        return get_flip_point(pancake_stack, first_blank) if first_blank is not None else None

    first_following_happy = find_pancake_index(pancake_stack, Pancake.HAPPY, start)
    if first_following_happy is None:
        return len(pancake_stack)
    else:
        return first_following_happy


def find_pancake_index(pancake_stack, is_happy, start=0):
    for i in range(start, len(pancake_stack)):
        pancake = pancake_stack[i]
        if pancake.is_happy == is_happy:
            return i
    return None


if __name__ == '__main__':
    main()
