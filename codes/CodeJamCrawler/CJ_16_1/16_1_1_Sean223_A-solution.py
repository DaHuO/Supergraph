__author__ = 'sean'


# IN_FILE = 'test_input.txt'
# OUT_FILE = 'test_output.txt'

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
    s = next(it).strip()
    letters = [s[i] for i in range(len(s))]

    answer = ""
    for letter in letters:
        if answer == "":
            answer += letter
        elif answer[0] <= letter:
            answer = letter + answer
        else:
            answer += letter

    line = "Case #{0}: {1}\n".format(str(case+1), str(answer))
    output += line


with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
