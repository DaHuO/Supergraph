infile = open("input1", "r")

outfile = open("output1", "w")

lines = infile.readlines()
linenum = lines[0]


for i,line in enumerate(lines[1:]):
    
    loops = 0
    init_number = int(line)
    
    if init_number == 0:
        outfile.write("Case #" + str(i+1) + ": INSOMNIA\n")

    else:
        digit_list = []
    
        while len(digit_list) != 10:
            loops += 1
            number = init_number * loops
            digits = map(int, str(number))

            for digit in digits:
                if not digit in digit_list:
                    digit_list.append(digit)
    
        outfile.write("Case #" + str(i+1) + ": " + str(number) + "\n")
