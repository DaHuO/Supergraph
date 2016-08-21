file_strings = []
import math
with open("Senate_Evacuation.txt") as data_file:
    for line in data_file:
        file_strings.append(line.strip())
test_case_number = int(file_strings[0])
file_strings.pop(0)

case = 1

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K ','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',' W', 'X', 'Y', 'Z']


for i in range(test_case_number):
    parties = int(file_strings.pop(0))
    numbers = [int(x) for x in file_strings.pop(0).strip().split()]
    chars = []
    while any(numbers):
        ind = numbers.index(max(numbers))
        numbers[ind] -= 1
        a = letters[ind]
        if sum(numbers) > 2 or sum(numbers) == 1:
            ind = numbers.index(max(numbers))
            numbers[ind] -= 1
            b = letters[ind]
        else:
            b = ""
        chars.append(a + b)

    print("Case #{}: {}".format(case, " ".join(chars)))

    case += 1
