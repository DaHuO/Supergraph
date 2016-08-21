
small_data_set = 10
large_data_set = 100

swap_count = 0


def main():
    t = int(input())
    if not 1 <= t or not t <= 100:
        print('1 <= T <= 100')
        return

    for i in range(1, t + 1):
        global swap_count
        swap_count = 0
        pancakes = list(input())

        for index in range(len(pancakes)):
            pancake = pancakes[index]

            # case 1: -+
            if pancake == '-':
                try:
                    next_pancake = pancakes[index+1]
                    if next_pancake == '+':
                        pancakes = recursive_swap(pancakes, index)
                except:
                    pancakes = recursive_swap(pancakes, index)

            # case 2: +-
            elif pancake == '+':
                try:
                    next_pancake = pancakes[index+1]
                    if next_pancake == '-':
                        pancakes = recursive_swap(pancakes, index)
                except:
                    pass

            # check pancakes
            if '-' not in pancakes:
                print('Case #{}: {}'.format(i, swap_count))
                break


def recursive_swap(pancakes, end_index):
    global swap_count
    for index in range(end_index+1):
        pancake = pancakes[index]
        pancakes[index] = '+' if pancake == '-' else '-'
    swap_count += 1
    return pancakes


main()

