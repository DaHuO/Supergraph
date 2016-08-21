import fileinput as fi

def count_sheep(n):
    curr = 0
    itr = 0
    digits = set()

    while len(digits) != 10:
        curr += 1
        itr += 1
        for digit in str(curr * n):
            digits.add(digit)
        if curr * n == (curr - 1) * n:
            return "INSOMNIA"

    return curr * n

curr_case = 0
for line in fi.input():
    if curr_case is 0:
        curr_case += 1
        continue
    n = int(line.strip())
    print("Case #%s: %s" % (curr_case, count_sheep(n)))
    curr_case += 1
