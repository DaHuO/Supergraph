
filepath = "C:/CodeJam/"
filename = "B-large.in"
output_file = open(filepath+"output.txt", "w")
with open(filepath+filename, "r") as input_file:
    test_cases = int(input_file.readline())
    for case_number, line in enumerate(input_file):
        last_char = "+"
        flips_required = 0
        if case_number >= test_cases:
            break
        for char in reversed(line.strip()):
            if char != last_char:
                last_char = char
                flips_required += 1
        output_file.write("Case #" + str(case_number+1) + ": " + str(flips_required)+"\n")




