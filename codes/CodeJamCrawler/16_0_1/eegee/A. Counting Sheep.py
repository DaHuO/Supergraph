import time
import datetime
__author__ = 'eegee'

filename = "A-large"

input_data = open("../data/" + filename + ".in")
output_data = open("../data/" + filename + ".out", "w")
time.perf_counter()

for case in range(int(input_data.readline())):
    # read inputs #
    n = int(input_data.readline())
    # read inputs #

    # solution #
    if n == 0:
        answer = "INSOMNIA"
    else:
        missing = set("0123456789")
        i, counting = 0, n
        while missing:
            i += 1
            counting = i * int(n)
            missing -= set(str(counting))
        answer = counting
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