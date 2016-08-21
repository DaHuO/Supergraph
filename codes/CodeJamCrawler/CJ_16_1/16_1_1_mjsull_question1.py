import sys

out = open(sys.argv[2], 'w')
with open(sys.argv[1]) as in_file:
    case_no = int(in_file.readline())
    for i in range(1, case_no + 1):
        s = in_file.readline().rstrip()
        newstring = s[0]
        first = s[0]
        for j in s[1:]:
            if j >= first:
                newstring = j + newstring
                first = j
            else:
                newstring = newstring + j
        out.write('Case #' + str(i) + ': ' + newstring + '\n')
    out.close()


