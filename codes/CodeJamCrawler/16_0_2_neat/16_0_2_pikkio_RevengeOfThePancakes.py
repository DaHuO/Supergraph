input_file = open("B-large.in", "r")
output_file = open("results.txt", "w+")

T = int(input_file.readline())

for i in range(0, T):
    line = input_file.readline()
    line = list(line)[:-1]
    line_length = len(line)
    
    flipcount = 0
    end_flag = True
    j = 0
    while j < line_length:
        #print(str(j) + " -> " + str(line))
        #print(str(line[line_length - 1 - j]) + " " + str(line[0]) + " " + str(end_flag))
        if (end_flag and (line[line_length - 1 - j] == "+")):
            j += 1
            continue
        
        end_flag = False
        
        if (line[line_length - 1 - j] != line[0]):
            j += 1
            continue
        else:
            flipcount += 1
            bck = line[0:line_length - j]
            for k in range(line_length - j):
                if (bck[k] == "+"):
                    line[line_length - 1 - j - k] = "-"
                else:
                    line[line_length - 1 - j - k] = "+"
            end_flag = True
            j = 0

    output_file.write("Case #" + str(i+1) + ": " + str(flipcount) + "\n")
    #print(str(flipcount) + " " + str(line))

input_file.close()
output_file.close()