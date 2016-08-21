import sys
import os
import math

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def evacuate(cas, N, senators, output_file):
    res_string = "Case #" + str(cas) + ":"
    nb_senators = sum(senators)
    
    while nb_senators > 0 :
        res_string += " "
        
        max_party = senators.index(max(senators))
        senators[max_party] -= 1
        res_string += alphabet[max_party]
        nb_senators -= 1
        
        if nb_senators != 2 :
            max_party = senators.index(max(senators))
            senators[max_party] -= 1
            res_string += alphabet[max_party]
            nb_senators -= 1
    
    output_file.write(res_string + "\n")

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
    senators = input_file.readline().rstrip().split(" ")
    senators = [int(i) for i in senators]
    evacuate(cas, N, senators, output_file)


input_file.close()
output_file.close()
