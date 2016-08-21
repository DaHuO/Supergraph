file = open("1large.in", "r")
lines = file.readlines()
del lines[0]
cases = 0
numbers = ['0','1','2','3','4','5','6','7','8','9']
for line in lines:
    cases += 1
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    timer = 0
    digits = str(line.rstrip())
    while numbers != [] and timer < 200:
        digits = str((timer+1) * int(line.rstrip()))
        for digit in range(0,len(digits)):
            if digits[digit] in numbers:
                numbers.remove(digits[digit])
        timer += 1
    if timer == 200:
        print("Case #",end="")
        print(cases, end="")
        print(": INSOMNIA")
    else:
        print("Case #",end="")
        print(cases, end="")
        print(":",digits)
