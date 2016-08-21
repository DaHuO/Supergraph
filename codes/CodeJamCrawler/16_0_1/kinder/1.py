
test_case = []
with open('A-large.in.txt', 'r') as file:
    for line in file:
        for n in line.split():
            test_case.append(n)

for i in range(int(test_case[0])):
    d = set()
    for j in list(test_case[i + 1]):
        d.add(j)

    k = 2
    while True:
        temp = len(d)

        for j in list(str(int(test_case[i + 1]) * k)):
            d.add(j)

        if int(test_case[i + 1]) == 0:
            print "Case #" + str(i + 1) + ": INSOMNIA"
            break
        elif len(d) == 10:
            print "Case #" + str(i + 1) + ": " + str(int(test_case[i + 1]) * k)
            break

        k += 1


