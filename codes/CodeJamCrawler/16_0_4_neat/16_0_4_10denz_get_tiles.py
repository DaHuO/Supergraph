import math

def main():
    with open('D-small-attempt1.in') as data:
        test_cases = int(data.readline())
        for idx in range(test_cases):
            base_length, complexity, max_lookups = [
                int(number) for number in data.readline().split()]
            needed_lookups = min_lookups(base_length, complexity)
            if needed_lookups > max_lookups:
                print('Case #{}: IMPOSSIBLE'.format(idx + 1))
            else:
                tiles = get_tiles(base_length, complexity)
                print('Case #{}: {}'.format(
                    str(idx + 1), ' '.join([str(tile) for tile in tiles])))


def get_tiles(base_length, complexity):
    if complexity == 1:
        return list(range(1, base_length + 1))
    tiles = []
    needed_lookups = min_lookups(base_length, complexity)
    for counter in range(1, needed_lookups + 1):
        tiles.append(counter * base_length - (counter - 1))
    return [int(number) for number in tiles]


def min_lookups(base_length, complexity):
    if complexity == 1:
        return base_length
    else:
        return math.ceil(base_length / 2)

if __name__ == '__main__':
    main()
