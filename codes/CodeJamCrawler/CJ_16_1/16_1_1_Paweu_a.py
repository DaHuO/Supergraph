data = open('a.in', 'r').readlines()
data = data[1:]


output = ""
for i in range(len(data)):
    outstr = "" + data[i][0]
    for j in range(1,len(data[i])):
        if data[i][j] >= outstr[0]:
            outstr = data[i][j] + outstr
        else:
            outstr = outstr + data[i][j]

    output += "Case #{}: {}".format(i + 1, outstr)
f = open('ala.out', 'w')
f.write(output)
