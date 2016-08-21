infile = open("A-large.in", "r")
cases = int(infile.readline().rstrip("\n"))

for i in range(cases):
    nextcase = int(infile.readline().rstrip("\n"))
    outfile = open("answer.txt","a")
    outfile.write("Case #{}: ".format(i+1))
    x = []
    for j in range(nextcase):
        x.append(chr(j+65))
    y = infile.readline().split()
    for j in range(len(y)):
        y[j] = int(y[j])
    checked = True
    while checked:
        checked = False
        highest = 0
        highestnumber = 0
        secondnumber = 0
        total = 0
        count = 0
        for k in range(len(y)):
            if y[k] > highest:
                highest = y[k]
                highestnumber = k
                checked = True
            total += y[k]
        if highest == 0:
            break
        for k in range(len(y)):
            if y[k] == highest and k != highestnumber:
                secondnumber = k
            if y[k] == highest and highest == 1:
                count += 1
        if highest != 1:
            if not secondnumber:
                y[highestnumber] -= 2
                outfile.write(x[highestnumber]+x[highestnumber]+" ")
            else:
                y[highestnumber] -= 1
                y[secondnumber] -= 1
                outfile.write(x[highestnumber]+x[secondnumber]+" ")
        else:
            if count == 3:
                y[highestnumber] -=1
                outfile.write(x[highestnumber]+" ")
            else:
                y[highestnumber] -= 1
                y[secondnumber] -= 1
                outfile.write(x[highestnumber]+x[secondnumber]+" ")
    outfile.write("\n")

    print()










    outfile.close()
infile.close()
