def strip_trailing_plus(line):
    while len(line) > 0 and line[-1:] == '+':
        line = line[:-1]
    return line

def get_plus_chain_end_index(line):
    index = -1
    while line[index+1] == '+':
        index += 1
    return index

def flip_pile_until_index_n(line, n):
    flipped = ''
    for pancake_index in range(n+1):
        flipped += '+' if line[n-pancake_index] == '-' else '-'
    return flipped + line[n+1:]

with open('B-large.in') as inp, open('output.out', 'w') as out:
    index = -2
    for line in inp:
        index += 1
        if index == -1: continue

        print('Case #'+str(index))
        print(line)
        line = line.strip()
        min_perm_number = 0
        line = strip_trailing_plus(line)
        while len(line) > 0:
            last_minus_index = get_plus_chain_end_index(line)
            if last_minus_index > -1:
                line = flip_pile_until_index_n(line, last_minus_index)
                min_perm_number += 1
            line = flip_pile_until_index_n(line, len(line)-1)
            line = strip_trailing_plus(line)
            min_perm_number += 1
        out.write('Case #%i: %i\n' % (index+1, min_perm_number))
