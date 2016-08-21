# Language       : Python 3
# Compiled Using : py_compile
# Version        : Python 3.4.3


def add_number(number, count):
    number_str = str(number)
    for char in number_str:
        count[int(char)] += 1


def is_done(count):
    for c in count:
        if c == 0:
            return False
    return True


with open("A-large.in") as f:
    data = f.readlines()

first = True
test_case_counter = 0
for line in data:
    if first:
        first = False;
        continue
    # Get rid of the \n at tht end.
    line = line[:-1]
    s = line.split(' ')

    n = int(s[0])
    test_case_counter += 1
    # Start of the real program:
    if n == 0:
        print("Case #" + str(test_case_counter) + ": INSOMNIA")
        continue
    counter = [0 for _ in range(10)]
    round = 0
    while not is_done(counter):
        round += 1
        add_number(round*n, counter)

    print("Case #" + str(test_case_counter) + ": " + str(round*n))
