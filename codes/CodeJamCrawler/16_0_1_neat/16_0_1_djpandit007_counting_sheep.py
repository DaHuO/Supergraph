f_in = open("A-large.in", "r")

num_case = int(f_in.readline())

data = []

for line in f_in:
    # Split data to store in list
    case = int(line.strip())

    if case == 0:
        data.append("INSOMNIA")
    else:
        digits = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
        i = 1
        while digits:
            lastNum = case * i
            digits.difference_update(set(str(lastNum)))
            i += 1
        data.append(lastNum)

outputFile = f_in.name.split('.')[0] + '-output'
f_out = open(outputFile, "w")

counter = 0
for value in data:
    f_out.write("Case #%s: %s\n" % (counter + 1, value))
    counter += 1

f_in.close()
f_out.close()
