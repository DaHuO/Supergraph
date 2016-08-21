import sys
import os
import math

def count_sheep(N) :
    if N == 0 :
        return 0
    Total = 0
    Tenfold = 0
    found = [False for i in range(10)]
    max_tested = int(math.pow(10, math.ceil(math.log10(N))+2))
    while Total <= max_tested :
        Total += N
        for car in str(Total) :
            found[int(car)] = True
        all_found = True
        for i in range(10) :
            all_found = (all_found and found[i])
        if all_found :
            return Total * 10**Tenfold
    return 0


if (len(sys.argv) < 2) :
    print("No input filename given.", file = sys.stderr)
    sys.exit(1)

input_filename = sys.argv[1]
if (len(sys.argv) > 2) :
    output_filename = sys.argv[2]
else :
    output_filename = os.path.splitext(input_filename)[0] + ".out"

try:
    input_file = open(input_filename, 'r')
except IOError:
    print("Unable to open " + input_filename + " for input.", file = sys.stderr)
    sys.exit(1)

try:
    output_file = open(output_filename, 'w')
except IOError:
    print("Unable to open " + output_filename + " for output.", file = sys.stderr)
    sys.exit(1)

T = int(input_file.readline().rstrip())

for cas in range(1, T+1) :
    N = int(input_file.readline().rstrip())
    Res = count_sheep(N)
    output_file.write("Case #" + str(cas) + ": ")
    if Res == 0 :
        output_file.write("INSOMNIA")
    else :
        output_file.write(str(Res))
    output_file.write("\n")

input_file.close()
output_file.close()
