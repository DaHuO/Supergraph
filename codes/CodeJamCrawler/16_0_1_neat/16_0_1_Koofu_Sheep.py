finished_at_count = 0
last_number_seen = ""
filepath = "C:/CodeJam/"
filename = "A-large.in"
output_file = open(filepath+"output.txt", "w")
with open(filepath+filename, "r") as input_file:
    test_cases = int(input_file.readline())
    for case_number, line in enumerate(input_file):
        number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if case_number >= test_cases:
            break
        for count in range(1, 100):
            print(line)
            holder = str(int(line) * count)
            for number_remaining in list(number_list):
                if number_remaining in holder:
                    if len(number_list) == 1:
                        last_number_seen = holder
                    number_list.remove(number_remaining)
            if not number_list:
                finished_at_count = count
                break
        if number_list:
            output_file.write("Case #" + str(case_number+1) + ": INSOMNIA\n")
        else:
            output_file.write("Case #" + str(case_number+1) + ": " + last_number_seen + "\n")
