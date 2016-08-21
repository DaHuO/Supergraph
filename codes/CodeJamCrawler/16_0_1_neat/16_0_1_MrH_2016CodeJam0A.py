# Open the given file 
lines = open("input.txt", "r").readlines()
n = int(lines[0].strip())

# The Big Idea is ...
def last_number(string):
    n = int(string)
    i = 1
    current_string = string
    seen_digit = [0,0,0,0,0,0,0,0,0,0]
    while i <= 1000000 and sum(seen_digit) < 10:
        for digit in current_string:
            seen_digit[int(digit)] = 1
        i = i + 1
        last = current_string
        current_string = str(i*n)
    if sum(seen_digit) == 10:
        return last
    else:
        return "INSOMNIA"

# Create a file for the answer and line by line write last number
# or INSOMNIA
outfile = open("answer.txt", "w")
for j in range(1,n+1):
    n = lines[j].strip()
    answer = last_number(n)
    line = "Case #" + str(j) + ": " + answer + "\n"
    outfile.write(line)
outfile.close()

