import sys
input_data = sys.stdin.readlines()

for case in range(1, len(input_data)):
    stack = input_data[case].replace("\n","").strip()

    flips = 0
    while "-" in stack:
        if stack[0] == "-":
            stack = stack.lstrip("-")
        else:
            stack = stack.lstrip("+")

        flips = flips + 1
    print("Case #"+str(case)+": "+ str(flips))