import time
import datetime
__author__ = 'eegee'

filename = "B-large"

input_data = open("../data/" + filename + ".in")
output_data = open("../data/" + filename + ".out", "w")
time.perf_counter()

for case in range(int(input_data.readline())):
    # read inputs #
    stack = list(input_data.readline().rstrip())
    # read inputs #

    answer = stack
    # solution #
    count = 0
    while True:
        if "-" not in stack:
            answer = count
            break

        size = 0
        previous = ""
        for pancake in stack:
            if previous and pancake != previous:
                break
            previous = pancake
            size += 1

        flipped_stack = ["-" if previous == "+" else "+"] * size
        stack = flipped_stack + stack[size:]
        count += 1
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