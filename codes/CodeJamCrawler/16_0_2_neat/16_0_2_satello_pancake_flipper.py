"""
Author: Sam Vitello
Google CodeJam Qualifiers 2016
Pancake Flipper
"""


def get_run_idx(cake_list, start_idx):
    """starting with an index return the index that the run stops
    """
    start_char = cake_list[start_idx]
    end_idx = start_idx + 1
    while cake_list[end_idx] == start_char:
        end_idx += 1
    return end_idx


def flipin_it(cake_list, idx):
    """takes a list of pancake faces [+, -, +, ...]
    flips the pancakes from left to right
    """
    for i, side in enumerate(cake_list[:idx]):
        cake_list[i] = (side+1) % 2
    return cake_list


def print_answer(answer_list):
    for t, num in enumerate(answer_list):
        print "Case #" + str(t+1) + ": " + str(num)


if __name__ == "__main__":
    iterations = int(raw_input())
    total_iter = []

    for _ in xrange(iterations):
        test_case = str(raw_input())
        pancakes = [0 if c == "-" else 1 for c in test_case]
        cur_idx = 0
        flip_count = 0

        # keep flippin until cake stack is one contiguous run
        while True:
            try:
                end_idx = get_run_idx(test_case, cur_idx)
                pancakes = flipin_it(pancakes, end_idx)
                flip_count += 1
                cur_idx = end_idx
            except IndexError:
                break

        # last flip if all face down
        if pancakes[0] == 0:
            flip_count += 1
        total_iter.append(flip_count)

    print_answer(total_iter)



