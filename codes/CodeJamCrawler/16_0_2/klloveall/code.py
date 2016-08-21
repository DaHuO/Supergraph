input_file = open("input.txt")
output = open("output.txt", "w")

n = int(input_file.readline())

for i in range(1, n + 1):
    stack = input_file.readline()

    last_char = stack[0]
    flips = 0
    for char in stack:
        if char == "\n":
            continue
        if char != last_char:
            flips += 1
            last_char = char

    if last_char == "-":
        flips += 1

    output.write("Case #" + str(i) + ": " + str(flips) + "\n")
