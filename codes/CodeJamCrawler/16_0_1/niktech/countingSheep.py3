import sys

test_cases = open(sys.argv[1], 'r')
n = -1
i = 1

for test in test_cases:
    numbers = []
    if n == -1:
        n = int(test)
        continue

    number = test.replace('\n', '').replace('\r', '')
    start = int(number)
    if number == "0":
        print("Case #" + str(i) + ": INSOMNIA")
        i += 1
        continue
    running = True
    while running:
        # add digits
        for letter in number:
            if letter not in numbers:
                numbers.append(letter)
            if len(numbers) == 10:
                print("Case #" + str(i) + ":", number)
                running = False
                i += 1
                break
        # new N
        number = str(int(number) + start)