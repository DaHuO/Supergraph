import fileinput

i = 0
num_cases = -1
for line in fileinput.input():
    if (i == 0):
        num_cases = int(line)
    else:
        count = 0
        prev = '0'
        line = line.rstrip()
        for c in line:
            if prev == '+' and c == '-':
                count+=1
            elif prev == '-' and c == '+':
                count+=1
            prev = c
        if prev == '-':
            count+=1
        print "Case #" + str(i) + ": " + str(count)
    i+=1
    if (i > num_cases):
        break