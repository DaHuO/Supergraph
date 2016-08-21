# Open the given file 
lines = open("input.txt", "r").readlines()
n = int(lines[0].strip())

# The Big Idea is ...
def number_of_flips(string):
    flips = 0
    if len(string) > 1:
        for i in range(len(string)-1):
            if string[i] != string[i+1]:
                flips = flips + 1
    if string[-1] == "-":
        flips = flips + 1
    return flips

# Create a file for the answer and line-by-line write
# the minimum number_of_flips needed
outfile = open("answer.txt", "w")
for j in range(1,n+1):
    answer = number_of_flips(lines[j].strip())
    line = "Case #" + str(j) + ": " + str(answer) + "\n"
    outfile.write(line)
outfile.close()

