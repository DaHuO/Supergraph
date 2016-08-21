def add_digits(number, digits):
    while number > 0:
        digits[number % 10] += 1
        number //= 10

fin = "input.txt"
fout = "output.txt"

tests = []
for line in open(fin, "r"):
    tests.append(int(line))
j = 0
with open(fout, "w") as f:
    for test in tests[1:]:
        j += 1
        finished = False
        digits = [0 for i in range(10)]
        
        for i in range(1, 101):
            add_digits(test * i, digits)
            if not any(map(lambda x: x == 0, digits)):
                f.write("Case #{}: {}\n".format(j, i * test))
                finished = True
                break
        if not finished:
            f.write("Case #{}: INSOMNIA\n".format(j))
    
        