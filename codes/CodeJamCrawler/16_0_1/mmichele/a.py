from sets import Set

count = 0
with open("test.dat") as f:
    lines = f.readlines()

for line in lines:
    n = int(line)

    if count > 0:
        s = Set()

        print "Case #" + str(count) + ":",
        for i in range(1, 1000):
            num = i * n
            for dig in map(int, str(num)):
                s.add(str(dig))
            if (len(s) == 10):
                print num
                break
        if i == 999:
            print "INSOMNIA"
    count += 1;
