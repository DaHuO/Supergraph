import sys


input = sys.stdin
input.readline() # number of inputs

count = 1
for line in input:
    number = int(line)
    digits = {}
    last_num = 0
    i = 1

    if number == 0:
        print("Case #{}: {}".format(count, "INSOMNIA"))
        count += 1
        continue

    while True:

        product = str(i*number)
        for letter in product:
            digits[letter] = None

        if(len(digits.keys())==10):
            last_num = number*i
            print("Case #{}: {}".format(count, last_num))
            break
        i += 1
    count += 1

