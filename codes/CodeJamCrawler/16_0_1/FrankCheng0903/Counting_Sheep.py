file_strings = []
with open("counting_sheep.txt") as data_file:
    for line in data_file:
        file_strings.append(int(line.strip()))

test_case_number = file_strings[0]
file_strings.pop(0)

output_results = []

for i in range(len(file_strings)):
    number = file_strings[i]
    length_of_num = int(len(str(number)))
    seen_numbers = []

    if number == 0:
        print("Case #{}: INSOMNIA".format(i + 1))
        continue

    seen = False
    for j in range(1, (10**(length_of_num + 1) + 1)):

        temp_num_str = str(j * number)
        for char in temp_num_str:
            if char not in seen_numbers:
                seen_numbers.append(char)
        if len(seen_numbers) == 10:
            print("Case #{}: {}".format(i + 1, temp_num_str))
            seen = True
            break
    if seen is False:
        print("Case #{}: INSOMNIA".format(i + 1))
