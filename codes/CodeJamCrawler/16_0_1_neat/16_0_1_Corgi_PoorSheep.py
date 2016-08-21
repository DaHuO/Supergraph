import string

fin = open('sheep.in', 'r')
fout = open('sheep.out', 'w')

t = int(fin.readline())

def check( digits ):
    res = True;
    for dig in string.digits:
        if digits.count(dig) == 0: res = False
    return res

def iter( num, digits ):
    for dig in list(str(num)):
        if digits.count(dig) == 0: digits.append(dig)
    return

for x in range(1, t + 1):
    n = int(fin.readline())
    i = 1

    result = "Case #{}: {}\n"

    if (n != 0):
        digits = []
        iter(n, digits)
        flag = check(digits)
        while not flag:
            i += 1
            iter(n*i, digits)
            flag = check(digits)
        result = result.format(x, n*i)
    else: result = result.format(x, "INSOMNIA")

    fout.write(result)