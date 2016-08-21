f = open("A-large.in", "rb")
lines = []

for line in f:
    lines.append(int(line))

for i in range(1, len(lines)):
    if lines[i] == 0:
        print "Case #" + str(i) + ": INSOMNIA"
    else:
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = lines[i]
        x = n
        while len(digits) > 0:
            for char in str(x):
                if digits.count(int(char)) > 0:
                    digits.remove(int(char))
            x += n
        print "Case #" + str(i) + ": " + str(x-n)
        
