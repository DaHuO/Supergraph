s = set(str(i) for i in range(10))
INPUT_FILE = "input.file"
OUTPUT_FILE = "output.file"
def calculate(input_):
    if input_ == 0:
        return "INSOMNIA"
    n = 1
    s2 = s.copy()
    while True:
        cur = n*input_
        s2.difference_update(str(cur))
        if not s2:
            return cur
        n += 1

with open(INPUT_FILE, "r") as f, open(OUTPUT_FILE, "w") as o:
    case_num = 0
    next(f)
    for line in f:
        case_num += 1
        o.write("Case #{}: {}\n".format(case_num, calculate(int(line))))