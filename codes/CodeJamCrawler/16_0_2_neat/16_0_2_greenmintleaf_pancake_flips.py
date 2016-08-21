from ucb import trace
results = {}


def is_happy(pancakes):
    return len(pancakes) == 0 or \
        all(pancake == '+' for pancake in pancakes)


def flip(pancakes):
    return ''.join(['-' if x == '+' else '+' for x in pancakes[::-1]])


def pancake_flips_dfs(pancakes):

    if pancakes in results and type(results[pancakes]) == str:
        return float('inf')
    elif pancakes in results and type(results[pancakes]) == int:
        return results[pancakes]
    else:
        results[pancakes] = 'Processing'

    if is_happy(pancakes):
        results[pancakes] = 0
        return 0

    min_flips = float('inf')
    for i in range(1, len(pancakes)+1):
        top = pancakes[:i]
        bottom = pancakes[i:]
        num_flips = 1 + pancake_flips_dfs(flip(top) + bottom)
        min_flips = min(min_flips, num_flips)

    results[pancakes] = min_flips
    return min_flips


def pancake_flips_bfs(pancakes):
    processing = {pancakes: True}
    pancakes_lst = [pancakes, '#']
    num_flips = 0
    while pancakes_lst:
        pancakes = pancakes_lst.pop(0)
        if pancakes == '#':
            num_flips += 1
            pancakes_lst.append('#')
            continue
        if is_happy(pancakes):
            return num_flips
        for i in range(1, len(pancakes)+1):
            top = pancakes[:i]
            bottom = pancakes[i:]
            if flip(top) + bottom not in processing:
                pancakes_lst.append(flip(top) + bottom)
                processing[flip(top) + bottom] = True

with open('B-small-attempt1.in', 'r') as small_file, open('B_output.txt', 'w') \
        as output_file:
    for index, pancakes in enumerate(small_file.readlines()[1:]):
        pancakes = pancakes.strip()
        output_file.write(
            'Case #{}: {}'.format(index+1, pancake_flips_bfs(pancakes)))
        output_file.write('\n')
