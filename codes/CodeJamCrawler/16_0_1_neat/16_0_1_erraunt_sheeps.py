

def num_digits(x):
    return list(str(x))


def last_num(x):
    if x == 0:
        return "INSOMNIA"
    A = set()
    cnum = x
    while True:
        for digit in num_digits(cnum):
            A.add(digit)
        if len(A) == 10:
            return cnum
        cnum += x

t = int(input())

for tc in range(1, t+1):
    num = int(input())
    print("Case #" + str(tc) + ": " + str(last_num(num)))





