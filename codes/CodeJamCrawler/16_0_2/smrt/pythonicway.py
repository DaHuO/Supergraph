answers = []


def jam(s):
    counter = 0
    symbol = s[0]
    for char in s:
        if char != symbol:
            counter += 1
            symbol = char
    if s[-1] == "-":
        counter += 1
    return counter

with open("B-large.in") as f:
    lines = f.readlines()[1:]
    for i, string in enumerate(lines, 1):
        answers.append("Case #{}: {}".format(i, jam(string.rstrip())))

with open("answers.txt", "w") as f:
    f.write("\n".join(answers))
