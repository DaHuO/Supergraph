def count_pancakes_same_face_from_top(pancakes):
    count = 0

    for i in range(0, len(pancakes)):
        if pancakes[i] == pancakes[0]:
            count += 1
        else:
            return count

    return count

def flip_n_first_pancakes(pancakes, n):
    pancakes = list(pancakes)
    first_half = pancakes[:n]
    first_half.reverse()
    pancakes = first_half + pancakes[n:]

    for i in xrange(0, n):
        if pancakes[i] == '+':
            pancakes[i] = '-'
        else:
            pancakes[i] = '+'

    return ''.join(pancakes)

def is_ready(pancakes):
    return all(pancake == '+' for pancake in pancakes)

def recurs_solve(pancakes, flips):
    if is_ready(pancakes):
        return [flips]

    ret = set()
    ret.update(recurs_solve(flip_n_first_pancakes(pancakes, count_pancakes_same_face_from_top(pancakes)), flips + 1))

    return ret

number_of_lines = int(raw_input())

for line in range(1, number_of_lines + 1):
    pile = raw_input()
    print 'Case #{}: {}'.format(line, min(recurs_solve(pile, 0)))
