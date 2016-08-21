import string


def check(res):
    for c in string.digits:
        if c not in res: return 0;
    return 1;


def result(test):
    if test == 0:
        return "INSOMNIA"
    number = test
    res = str(test)
    while not(check(res)):
        number += test
        res += str(number)
    return str(number)

#filename = input("Input name and location of input file: ")

problem = open("in.in", "r")

cases = int(problem.readline())

tests = []

for i in range(cases):
    tests.append(int(problem.readline()))

problem.close()

output = "out.out"

out = open(output, "w")

i = 1
for test in tests:
    out.write("Case #" + str(i) + ": ")
    out.write(result(test))
    out.write("\n")
    i += 1

out.close()

