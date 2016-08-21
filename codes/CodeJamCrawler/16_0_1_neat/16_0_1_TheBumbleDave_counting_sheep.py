def fall_asleep(initial_number_of_sheep):
    multiplier = 1
    all_digits_seen = False
    last_number_seen = initial_number_of_sheep
    digits_seen = {
        '0': False,
        '1': False,
        '2': False,
        '3': False,
        '4': False,
        '5': False,
        '6': False,
        '7': False,
        '8': False,
        '9': False,
        }

    while not all_digits_seen:
        last_number_seen = initial_number_of_sheep * multiplier
        number_string = str(last_number_seen)
        digits = number_string.__len__()
        for i in range(0, digits):
            digits_seen[number_string[i]] = True
        all_digits_seen = digits_seen['0']
        for i in range(1, 10):
            all_digits_seen = all_digits_seen and digits_seen[str(i)]
        multiplier += 1

    return last_number_seen

input_file = "A-large.in"
with open(input_file, 'r') as file_object_in:
    lines = file_object_in.readlines()
    testcases = int(lines[0].strip())
    case_number = 0
    output_file = "output.txt"
    while case_number < testcases:
        case_number += 1
        start_number = int(lines[case_number].strip())
        if start_number == 0:
            with open(output_file, 'a') as file_object_out:
                file_object_out.write("Case #" + str(case_number) + ": INSOMNIA\n")
        else:
            with open(output_file, 'a') as file_object_out:
                file_object_out.write("Case #" + str(case_number) + ": " + str(fall_asleep(start_number)) + "\n")