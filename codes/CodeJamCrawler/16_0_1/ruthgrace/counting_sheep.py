f = open('input.txt', 'r')

cases = int(f.readline())

for i in range(cases):
    n = int(f.readline())
    if (n == 0):
        print("Case #" + str(i + 1) + ": INSOMNIA")
    else:
        digits = [0] * 10
        filled = 0
        multiple = n;
        while (filled < 10):
            multiple = str(multiple)
            for c in multiple:
                if (digits[int(c)] == 0):
                    digits[int(c)] = 1
                    filled = filled + 1
            multiple = int(multiple) + n
        multiple = multiple - n
        print("Case #" + str(i + 1) + ": " + str(multiple))