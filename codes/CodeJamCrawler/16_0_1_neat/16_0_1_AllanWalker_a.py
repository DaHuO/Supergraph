import fileinput

def calculate(case, value):
    if value == 0:
        result = "INSOMNIA"
    else:
        result = 0
        visible = set()
        while True:
            result += value
            n = result
            while n:
                r, n = n % 10, n // 10
                visible.add(r)
            if len(visible) == 10:
                break
    print "Case #{}: {}".format(case, result)

case = -1
for line in fileinput.input():
    case += 1
    if case < 1:
        continue
    calculate(case, int(line))
