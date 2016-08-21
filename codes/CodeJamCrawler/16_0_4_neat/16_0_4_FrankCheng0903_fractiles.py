file_strings = []
with open("fractiles.txt") as data_file:
    for line in data_file:
        file_strings.append(line.strip())
test_case_number = file_strings[0]
file_strings.pop(0)

original_sizes = []
complexities = []
number_of_grads = []
for i in file_strings:
    item = i.split()
    original_sizes.append(int(item[0]))
    complexities.append(int(item[1]))
    number_of_grads.append(int(item[2]))


def easy_solve(original_size, complexity, number_of_tries):
    """
    Solve the puzzle and returns a list of positions when original_size is
    equal to number_of_tries. This is always possible.
    Precondition: original_size == number_of_tries
    @rtype: list[str]
    """
    # The only situation in which there's no gold is when the whole original
    # sequence was lead. If there was one gold tile in the original sequence
    # then that K^(C-1) subsection of the final sequence will be all gold.
    # Thus we will take a position in the middle of each subsection.
    subsection_len = original_size**(complexity-1)
    positions = []
    for i in range(original_size):
        j = 1/2 + i
        positions.append(str(int(j*subsection_len) + 1))
    return positions


def find_gold(original_size, complexity, number_of_tries):
    """
    Returns a string of positions to search, separated by whitespace,
    from 1 to original_size^complexity.
    Returns string "IMPOSSIBLE" if this is impossible.
    @rtype: str
    """
    if number_of_tries == original_size:
        list_of_pos = easy_solve(original_size, complexity, number_of_tries)
        return_string = " ".join(list_of_pos)
        return return_string


for i in range(len(original_sizes)):
    print("Case #{}: {}".format(i + 1, find_gold(original_sizes[i],
                            complexities[i], number_of_grads[i])))
