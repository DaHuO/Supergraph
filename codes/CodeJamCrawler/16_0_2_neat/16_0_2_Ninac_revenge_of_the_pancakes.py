import re


def main():
    file = open('B-large.in', 'rU')
    lines = iter(file.readlines())
    file.close()

    case_count = int(next(lines))
    output = open('output', 'w')
    for case_idx in range(case_count):
        flip_count = 0
        pancakes = next(lines).rstrip()

        while len(set(pancakes)) > 1:
            flip_idx = 1
            pancake = pancakes[0]

            while pancake is pancakes[flip_idx]:
                flip_idx += 1

            flip_stack = pancakes[:flip_idx]
            flip_stack = reversed(list(flip_stack))
            flip_stack = ''.join(list(map(flip_pancake, flip_stack)))

            pancakes = flip_stack + pancakes[flip_idx:]
            flip_count += 1

        if pancakes[0] is '-':
            flip_count += 1

        print('Case #{}: {}'.format(case_idx + 1, flip_count), file=output)
    output.close()


def flip_pancake(pancake):
    if pancake is '+':
        return '-'
    else:
        return '+'


if __name__ == '__main__':
    main()
