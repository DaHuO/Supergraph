__author__ = 'sean'


# IN_FILE = 'stress-input.txt'
# OUT_FILE = 'stress-output.txt'

# IN_FILE = 'A-small.in'
# OUT_FILE = 'small_out.txt'

IN_FILE = 'A-large.in'
OUT_FILE = 'large_out.txt'


with open(IN_FILE, 'r') as fileIn:
    fileLines = fileIn.readlines()

it = iter(fileLines)
numbCases = int(next(it))
output = ""


for case in range(numbCases):
    answer = ""
    counter = 1
    n = int(next(it).strip())
    current_number = n
    digits_seen = [str(i) in str(current_number) for i in range(10)]

    if n == 0:
        answer = "INSOMNIA"
    else:
        while not all(digits_seen):
            counter += 1
            current_number = n * counter
            for i in range(10):
                digits_seen[i] = digits_seen[i] or str(i) in str(current_number)
        answer = current_number

    line = "Case #{0}: {1}\n".format(str(case+1), str(answer))
    output += line


with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
