import csv
with open("4.in", "r", newline="") as infile:
    lines = csv.reader(infile, delimiter=" ")
##    del lines[0]
##    print(lines)
    cases = 0
    for line in lines:
        numbers = []
        cases += 1
##        digits = line.rstrip()
        k = int(line[0])
        c = int(line[1])
        for x in range(0,k):
            numbers.append(x+1)
        print("Case #",end="")
        print(cases,end="")
        print(":",end="")
        for x in numbers:
            print("",x,end="")
        print()
