infile = open("A-large.in", "r")
cases = infile.readline()
lines = infile.readlines()

numbers = []
answers = []

for line in lines:
    line = line.rstrip()
    numbers.append(line)
infile.close()

def Counting_Sheep(number):
    if number == 0:
        return "INSOMNIA"
    else:
        digits = []
        multiplier = 0
        while len(digits) < 10:
            multiplier += 1
            current = str(number*multiplier)
            current = list(current)
            for digit in current:
                if digit not in digits:
                    digits.append(digit)
        return number*multiplier

outfile = open("A-big-output.txt", "a")
for i in range(len(numbers)):
    answer = Counting_Sheep(int(numbers[i]))
    outfile.write("Case #%s: %s\n" % (i + 1, answer))
outfile.close()

