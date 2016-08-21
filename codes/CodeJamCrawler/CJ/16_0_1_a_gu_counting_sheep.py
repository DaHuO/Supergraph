def add_digits(number, digits):
    for digit in str(number):
        digits.add(digit)

f = open("A-large.in", "r")
f2 = open("out.txt", "w")
n = int(f.readline())
for i in range(n):
    digits = set()
    number = int(f.readline())
    if number == 0:
        copy = "INSOMNIA"
    else:
        copy = number
        counter = 1
        while len(digits) < 10:
            copy = number * counter
            add_digits(copy, digits)
            counter += 1
    if i != n - 1:
        output = "Case #" + str(i + 1) + ": " + str(copy) + "\n"
    else:
        output = "Case #" + str(i + 1) + ": " + str(copy)
    f2.write(output)
