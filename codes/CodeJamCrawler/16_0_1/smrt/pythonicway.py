answers = []
def jam(n):
    if n == 0:
        return "INSOMNIA"
    digits_seen = []
    i = 1
    while True:
        number = n * i
        digits = list(str(number))
        for digit in digits:
            if digit not in digits_seen:
                digits_seen.append(digit)
                if len(digits_seen) == 10:
                    return number
        i += 1
with open("A-large.in") as f:
    lines = f.readlines()[1:]
    for i, number in enumerate(lines, 1):
        answers.append("Case #{}: {}".format(i, jam(int(number))))

with open("answers.txt", "w") as f:
    f.write("\n".join(answers))
