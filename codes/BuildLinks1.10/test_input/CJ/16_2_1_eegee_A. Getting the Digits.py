import datetime
import time

__author__ = 'eegee'

filename = "A-large"

input_data = open("../data/" + filename + ".in")
output_data = open("../data/" + filename + ".out", "w")
time.perf_counter()

text_numbers = ["ZERO", "SIX", "TWO", "EIGHT", "ONE", "FOUR", "FIVE", "THREE", "SEVEN", "NINE"]
lookup = {"ZERO": 0,
          "ONE": 1,
          "TWO": 2,
          "THREE": 3,
          "FOUR": 4,
          "FIVE": 5,
          "SIX": 6,
          "SEVEN": 7,
          "EIGHT": 8,
          "NINE": 9}

for case in range(int(input_data.readline())):
    # read inputs #
    input_string = input_data.readline().strip()
    # read inputs #

    # solution #
    input_copy = input_string
    skip = -1
    while input_copy:
        input_copy = input_string
        answer = []
        skip_copy = skip
        for text_number in text_numbers:
            found = True
            while found:
                for text_char in list(text_number):
                    if text_char not in input_copy:
                        found = False
                        break
                else:
                    if len(answer) == skip_copy:
                        skip_copy = -1
                        found = False
                        continue
                    # print(text_number)
                    answer.append(lookup[text_number])
                    for text_char in list(text_number):
                        input_copy = input_copy.replace(text_char, "", 1)
        skip += 1
    answer.sort()
    answer = "".join(map(str, answer))
    # solution #

    # display and write output #
    output_line = "Case #" + str(case + 1) + ": "
    print(output_line + str(answer))
    output_data.write(output_line + str(answer) + "\n")
    # display and write output #

print()
print("total_time:", datetime.timedelta(seconds=time.perf_counter()))
input_data.close()
output_data.close()
