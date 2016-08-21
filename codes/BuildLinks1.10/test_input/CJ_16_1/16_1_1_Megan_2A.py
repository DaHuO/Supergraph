import fileinput

i = 0
num_cases = -1
for line in fileinput.input():
    if (i == 0):
        num_cases = int(line)
    else:
        result = ""
        for c in line.rstrip():
            if result == "":
                result += c
            else:
                if result[0] <= c:
                    result = c + result
                else:
                    result += c

        print "Case #" + str(i) + ": " + result

    i+=1
    if (i > num_cases):
        break