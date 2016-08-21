count = 0
with open("test2.dat") as f:
    lines = f.readlines()

for line in lines:
    if count > 0:
        print "Case #" + str(count) + ":",

        line = line.strip()
        passi = 0
        i = 0 
        for i in range(1, len(line)):
            curr = line[i-1]
            nex = line[i]
            if curr != nex:
                passi += 1

        if line[i] == "-":
            passi += 1
        print passi

    count += 1;
