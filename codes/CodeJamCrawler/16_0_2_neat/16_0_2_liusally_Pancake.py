of = open('pancake-large.out', 'w')


def flip(ch):
    if ch == '+':
        return '-'
    else:
        return '+'

with open('B-large.in', 'r') as f:
    count = int(f.readline().rstrip('\n'))
    for i in range(count):
        line = f.readline().rstrip('\n')

        flip_count = 0
        current_ch = line[0]
        for current in range(len(line)):
            if not line[current] == current_ch:
                flip_count += 1
                current_ch = flip(current_ch)

        if current_ch == '-':
            flip_count += 1

        of.write('Case #{}: {}\n'.format(i + 1, flip_count))









