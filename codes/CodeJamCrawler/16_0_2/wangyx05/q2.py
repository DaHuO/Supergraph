def minflip(input):
    # flip[0] is the min num needed to flip to +
    # flio[1] is the min mun needed to flip to -
    if input[0] == "+":
        flip = [0, 1]
    else:
        flip = [1, 0]
    for i in range(1, len(input)):
        if input[i] == "-" and input[i - 1] == "+":
            flip[0] = flip[1] + 1
        if input[i] == "+" and input[i - 1] == "-":
            flip[1] = flip[0] + 1
    return flip[0]


input = []
output = []
with open("B-large.in") as f:
    n = int(f.readline())
    for l in f:
        input.append(l)

for s in input:
    output.append(minflip(s))

with open("output.out", "w") as f:
    for i in range(n):
        f.write("Case #" + str(i+1) + ": " + str(output[i]) + "\n")
