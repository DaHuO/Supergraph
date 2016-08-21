__author__ = 'sean'


# IN_FILE = 'test_input.txt'
# OUT_FILE = 'test_output.txt'

# IN_FILE = 'B-small.in'
# OUT_FILE = 'small_out.txt'

IN_FILE = 'B-large.in'
OUT_FILE = 'large_out.txt'


def find_missing(all_lists):
    if len(all_lists) == 1:
        return all_lists[0]

    sorted_lists = sorted(all_lists, key=lambda x: x[0])
    least_value = sorted_lists[0][0]

    if least_value == sorted_lists[1][0]:
        smaller_lists = [p[:] for p in sorted_lists[2:]]
        for small_list in smaller_lists:
            del small_list[0]
        end_of_missing_list = find_missing(smaller_lists)

        possible_first_numbers = sorted_lists[0][1:]
        for other_possibility in sorted_lists[1][1:]:
            possible_first_numbers.append(other_possibility)
        for other_list in sorted_lists[2:]:
            possible_first_numbers.remove(other_list[0])
        end_of_missing_list.insert(0, possible_first_numbers[0])
        return end_of_missing_list

    else:
        missing_list = [q[0] for q in sorted_lists]
        for z in sorted_lists[0][1:]:
            missing_list.remove(z)
        return missing_list

with open(IN_FILE, 'r') as fileIn:
    fileLines = fileIn.readlines()

it = iter(fileLines)
numbCases = int(next(it))
output = ""


for case in range(numbCases):
    n = int(next(it))
    lists = []
    for i in range(2 * n - 1):
        next_list = [int(j) for j in next(it).strip().split()]
        lists.append(next_list)

    answer_list = find_missing(lists)
    answer = ""
    for val in answer_list:
        answer += str(val) + ' '

    line = "Case #{0}: {1}\n".format(str(case+1), str(answer))
    output += line


with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
