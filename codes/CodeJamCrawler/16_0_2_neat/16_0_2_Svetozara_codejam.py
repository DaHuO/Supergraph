import string
import re


def check(res):
    if '-' in res:
        return 0;
    return 1;


def flip(n, res):
    res = res[:n].replace("-","0") + res[n:]
    res = res[:n].replace("+","-") + res[n:]
    res = res[:n].replace("0","+") + res[n:]
    return res


def result(test):
    if test == "+":
        return 0
    if test == "-":
        return 1
    if check(test):
        return 0
    tries = 10000000
    sad_faces = re.finditer("[-]+", test)
    pos = []
    for face in sad_faces:
        pos.append(face.end())
    for position in pos:
        trial = 1 + result(flip(position, test))
        if trial < tries:
            tries = trial
    return tries

#filename = input("Input name and location of input file: ")

problem = open("in.in", "r")

cases = int(problem.readline())

tests = []

for i in range(cases):
    tests.append(problem.readline().rstrip('\n'))

problem.close()

output = "out.out"

out = open(output, "w")

i = 1
for test in tests:
    out.write("Case #" + str(i) + ": ")
    out.write(str(result(test)))
    out.write("\n")
    i += 1

out.close()

