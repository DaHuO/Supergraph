__author__ = 'sean'


# IN_FILE = 'test_input.txt'
# OUT_FILE = 'test_output.txt'

IN_FILE = 'D-small.in'
OUT_FILE = 'small_out.txt'

# IN_FILE = 'D-large.in'
# OUT_FILE = 'large_out.txt'


with open(IN_FILE, 'r') as fileIn:
    fileLines = fileIn.readlines()

it = iter(fileLines)
numbCases = int(next(it))
output = ""


for case in range(numbCases):
    answer = ""

    (k, c, s) = (int(value) for value in next(it).strip().split())

    if k == 1:
        answer = "1"
    else:
        total_tiles = k**c

        if c == 1:
            gap_size = 1
        else:
            gap_size = (total_tiles - k) // (k-1) + 1

        current = 1
        for i in range(1, k+1):
            answer += str(current) + ' '
            current += gap_size

    line = "Case #{0}: {1}\n".format(str(case+1), str(answer))
    output += line


with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
