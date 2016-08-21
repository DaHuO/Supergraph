# Daniele Perazzolo April 2016
# Code Jam 2016


def problem(plate):
    flips = 0
    token = plate[0]
    if plate[len(plate)-1] == "-":
        flips += 1
    for pointer in range(0, len(plate)):
        if plate[pointer] != token:
            flips += 1
            if token == "+":
                token = "-"
            else:
                token = "+"
    return flips


t = int(input()) #Test Cases
for i in range(1, t + 1):
    pancakes = input()
    print("Case #{}: {}".format(i, problem(pancakes)))