file_strings = []
with open("pancakes.txt") as data_file:
    for line in data_file:
        file_strings.append(line.strip())

test_case_number = file_strings[0]
file_strings.pop(0)

def count_flips(pancakes):
    """
    Counts the number of inversions between - and +. Adds 1 if the last
    character is a -
    @param str pancakes:
    @rtype int
    """
    count = 0
    if pancakes[-1] == "-":
        count += 1
    for i in range(len(pancakes) - 1):
        if pancakes[i] != pancakes[i + 1]:
            count += 1
    return count

for i in range(len(file_strings)):
    print ("Case #{}: {}".format(i + 1, count_flips(file_strings[i])))
