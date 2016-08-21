from __future__ import print_function
numbers = []
with open("A-large.in") as reader:
    for line in reader:
        numbers.append(int(line))
outfile = open("out.txt", 'a')

counter = 1
solved = False
for number in numbers[1:]:
    solved = False
    numbersseen = []
    currentnumber = 0
    for i in range(1, 101):
        currentnumber = i * number
        currentdigits = [int(d) for d in str(currentnumber)]
        numbersseen.extend([x for x in currentdigits if x not in numbersseen])
        if set(numbersseen) == set(range(0, 10)):
            solved = True
            break

    if solved:
        print("Case #" + str(counter) + ": " + str(currentnumber), file=outfile)
    else:
        print("Case #" + str(counter) + ": INSOMNIA", file=outfile)
    counter += 1
