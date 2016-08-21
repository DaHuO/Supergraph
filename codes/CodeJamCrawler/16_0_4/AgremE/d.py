input_file = open("D-small-attempt0.in")
output_file = open("solution.txt", "w")
t = int(input_file.readline().strip())
for i in range(t):
    output_file.write("Case #" + str(i+1) + ": ")
    s = input_file.readline().strip().split(" ")
    for j in range(int(s[0])):
        output_file.write(str(j+1)+" ")
    output_file.write("\n")
output_file.close()